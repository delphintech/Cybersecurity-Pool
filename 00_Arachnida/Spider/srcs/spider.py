import os
import requests
import beautifulsoup4

class Spider:

	def __init__(self, args):
		self.url = ""
		self.path = "./data/"
		self.depth = 0
		self.done = []

		opt = ""
		i = 0
		while i < len(args):
			if (args[i][0] == '-'):
				if len(args[i]) < 2:
					raise ValueError("Bad option call")
				
				match args[i][1]:
					case 'r':
						if 'r' in opt:
							raise ValueError("Duplication option r")
						opt += "r"
						if 'l' not in opt:
							self.depth = 5
					case 'l':
						if 'l' in opt:
							raise ValueError("Duplication option l")
						opt += "l"
						i += 1
						self.depth = int(args[i])
					case 'p':
						if 'p' in opt:
							raise ValueError("Duplication option p")
						opt += "p"
						i += 1
						self.path = args[i]
					case _:
						raise ValueError("Wrong option")
			else:
				if i < len(args) - 1:
					raise ValueError("URL should be last")
				self.url = args[i]
			i += 1
		self.check(opt)

	def check(self, opt):
		''' Check for option validity '''
		if 'l' in opt and 'r' not in opt:
			raise ValueError("Depth option without recursive")
		if 'l' in opt and (self.depth < 0 or self.depth > 1000):
			raise ValueError("Invalid depth (must be between 0 and 1000)")
		
		''' Check for folder path '''


		''' Check if url is valid '''

void	Spider::check(string opt) {

	# Check if options validity
	if (opt.find("l") != string::npos && opt.find("r") == string::npos)
		throw invalid_argument("Depth option without recursive");
	if (opt.find("l") != string::npos && (depth < 0 || depth > 1000))
		throw invalid_argument("Invalid depth (must be between 0 and 1000)");
	# Check for folder path validity
	int	check = mkdir(this->path.c_str(), 0777);
	if (this->path.back() != '/')
		this->path += "/";
	if (check < 0 && errno != EEXIST)
		throw invalid_argument("Unable to create directory \"" + this->path + "\"");
	# Check if URL is valid
	if (url.empty())
    	throw invalid_argument("No URL");
	# CURL *curl = curl_easy_init();
	# if(curl) {
	# 	curl_easy_setopt(curl, CURLOPT_URL, this->url.c_str());
	
	# 	CURLcode res = curl_easy_perform(curl);
	# 	if (res != CURLE_OK) {
	# 		curl_easy_cleanup(curl);
	# 		throw std::invalid_argument("URL invalid or not responding");
	# 	}
	# 	curl_easy_cleanup(curl);
	# }
}


void	Spider::scrap(const string url) {
	vector<string>	links;
	vector<string>	imgs;
	string			content;

	if (find(this->done.begin(), this->done.end(), url) != this->done.end())
		return ;
	# Get the page
	CURL *curl = curl_easy_init();
	if(!curl)
		throw exception();
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_to_string);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, &content); 
    CURLcode res = curl_easy_perform(curl);
	
	if (res != CURLE_OK)
		throw runtime_error(url + " is invalid or not responding");

	curl_easy_cleanup(curl);

	# Parse to get each image url
	imgs = parse_get_all(content, "#img[@src]", "src");

	# Download every images
	for (int i = 0; i < (int)imgs.size(); i++) {
		this->download_img(imgs[i]);
	}

	# Push url to done list
	this->done.push_back(url);

	if (this->depth > 0) {
		# Parse to get each link in the page
		links = parse_get_all(content, "#a[@href]", "href");
		this->depth--;
		# Scrap every links
		for (int i = 0; i < (int)links.size(); i++) {
			this->scrap(links[i]);
		}
	}
}

void		Spider::download_img(const string url) {
	string	filename;

	filename = get_img_name(url);
	if (filename.empty())
		return ;
	
	filename = this->path + filename;
    CURL* curl = curl_easy_init();
    if (curl) {
        FILE* fp = fopen(filename.c_str(), "wb");
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        CURLcode res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        fclose(fp);

        if (res != CURLE_OK)
            throw runtime_error(url + "Could not download: " + url);
	}
}