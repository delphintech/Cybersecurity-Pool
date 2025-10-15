#ifndef UTILS_HPP
#define UTILS_HPP

#include <iostream>
#include <vector>
#include <algorithm>
#include <sys/stat.h>
#include <fstream>
#include "curl/curl.h"
#include <libxml/HTMLparser.h>

using namespace std;

#define	USAGE "usage: ./spider [options] URL\n \
	options:\n\
		-r, recursively downloads the images in the URL\n\
		-r -l [N], indicates the maximum depth level of the recursive download. Default is 5\n\
		-p [PATH], indicates the path where the downloaded files will be saved.Default: ./data"

size_t			write_to_string(void *ptr, size_t size, size_t nmemb, void *userdata);
size_t			write_data(void* ptr, size_t size, size_t nmemb, FILE* stream);
vector<string>	parse_get_all(string content, string Xpath, string attribute);
string			get_img_name(string	img_url);

#endif