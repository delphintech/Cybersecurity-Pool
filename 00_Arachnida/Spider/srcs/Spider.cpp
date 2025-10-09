#include <iostream>
#include "Spider.hpp"

const string	Spider::get_url() const {
	return this->url;
}

Spider::Spider(int ac, char **av) : path("./data/"), depth(0) {
	string	opt;
	string	arg;

	for (int i = 1; i < ac; i++) {
		arg = av[i];

		if (arg[0] == '-') {
			if (arg.length() != 2)
				throw invalid_argument("Bad option call");
			if (arg[0] == 'r') {
				if (opt.find("r") != string::npos)
					throw invalid_argument("Duplication option r");
				opt += "r";
				if (opt.find("l") == string::npos)
					depth = 5;
			} else if (arg[0] == 'l') {
				if (opt.find("l") != string::npos)
					throw invalid_argument("Duplication option l");
				opt += "l";
				depth = stoi(av[++i]);
			} else if (arg[0] == 'p') {
				if (opt.find("l") != string::npos)
					throw invalid_argument("Duplication option p");
				opt += "p";
				path = av[++i];
			} else {
				throw invalid_argument("Wrong options");
			}
		} else {
			if (i != ac - 1)
				throw invalid_argument("URL should be last");
			url = av[i];
		}
	}
	this->check(opt);
}

Spider::~Spider() {}

void	Spider::check(string opt) {
	// Check if options validity
	if (opt.find("l") != string::npos && opt.find("r") == string::npos)
		throw invalid_argument("Depth option without recursive");
	if (opt.find("l") != string::npos && (depth < 0 || depth > 1000))
		throw invalid_argument("Invalid depth (must be between 0 and 1000)");
	// Check for folder path validity
	int	check = mkdir(this->path.c_str(), 0777);
	if (check < 0 && errno != EEXIST)
		throw invalid_argument("Unable to create directory \"" + this->path + "\"");
	// Check if URL is valid
	CURL *curl = curl_easy_init();
	if(curl) {
		curl_easy_setopt(curl, CURLOPT_URL, this->url.c_str());
	
		CURLcode res = curl_easy_perform(curl);
		if (res != CURLE_OK) {
			curl_easy_cleanup(curl);
			throw std::invalid_argument("URL invalid or not responding");
		}
		curl_easy_cleanup(curl);
	}
}

void	Spider::scrap(const string url) {
	vector<string>	urls;
	vector<string>	imgs;

	// Get the page
	CURL *curl = curl_easy_init();
	if(!curl)
		throw exception();
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    CURLcode res = curl_easy_perform(curl);
	
	// TODO: parse to get each image url

	// TODO: download every images

	if (this->depth > 0) {
		// TODO: parse to get each link if depth > 0
	
		this->depth--;
		// TODO: scrap every url if not already in this->done
	}


    curl_easy_cleanup(curl);
}