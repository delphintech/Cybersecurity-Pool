#include "utils.hpp"

// Write to string function for curl
size_t write_to_string(void *ptr, size_t size, size_t nmemb, void *userdata) {
    std::string *str = static_cast<std::string*>(userdata);
    str->append(static_cast<char*>(ptr), size * nmemb);
    return size * nmemb;
}

size_t write_data(void* ptr, size_t size, size_t nmemb, FILE* stream) {
    size_t written = fwrite(ptr, size, nmemb, stream);
    return written;
}

string xpath_extract_string(xmlXPathContextPtr context, const char* xpath_expr) {
    xmlXPathObjectPtr result = xmlXPathEvalExpression((xmlChar*)xpath_expr, context);
    if (!result || result->nodesetval->nodeNr == 0)
        return "";

    xmlChar* content = xmlNodeGetContent(result->nodesetval->nodeTab[0]);
    string value = string(reinterpret_cast<char*>(content));
    xmlFree(content);
    xmlXPathFreeObject(result);
    return value;
}

// Extract the string attribute of all the Xpath
vector<string>	parse_get_all(string content, string Xpath, string attribute) {
	htmlDocPtr 		doc;
	vector<string>	results = {};

	doc = htmlReadMemory(content.c_str(), content.length(), nullptr, nullptr, HTML_PARSE_NOERROR);
	if (!doc)
        throw runtime_error("Failed to parse HTML document");
	
  // Instantiate XPath context
	xmlXPathContextPtr context = xmlXPathNewContext(doc);
	if (!context) {
		xmlFreeDoc(doc);
        throw runtime_error("Failed to parse HTML document");
	}

	// Fetch all elements matching the given XPath
  	xmlXPathObjectPtr elements = xmlXPathEvalExpression((xmlChar *)Xpath.c_str(), context);
	if (!elements) {
		xmlXPathFreeContext(context);
		xmlFreeDoc(doc);
		throw runtime_error("Failed to parse HTML document");
	}

	if (elements->nodesetval == NULL)
		return results;
	
	// Iterate over the elements to store them in the vector
	for (int i = 0; i < elements->nodesetval->nodeNr; ++i)
	{
		// Get element from list
		xmlNodePtr element = elements->nodesetval->nodeTab[i];

        xmlXPathSetContextNode(element, context);
		
		// extract data
		string data = xpath_extract_string(context, attribute.c_str());

		if (find(results.begin(), results.end(), data) == results.end())
			results.push_back(data);
	}

    // Free resources
    xmlXPathFreeObject(elements);
    xmlXPathFreeContext(context);
    xmlFreeDoc(doc);

	return results;
}

string	get_img_name(string	img_url) {
	string	extensions[5] = {".jpg", ".jpeg", ".png", ".gif", ".bmp"};
	string	ext = "";
	
	for (int i = 0; i < 5; i++) {
		if (img_url.size() < extensions[i].size())
			return ("");
		if (img_url.compare(img_url.size() - extensions[i].size(), extensions[i].size(), extensions[i]) == 0)
			ext = extensions[i];
	}

	if (ext.empty())
		return ("");
	
	size_t	pos = img_url.rfind('/');
	if (pos == string::npos)
		return img_url;
	return (img_url.substr(pos + 1));
}