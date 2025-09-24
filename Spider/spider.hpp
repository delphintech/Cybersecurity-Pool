#ifndef SPIDER_HPP
#define SPIDER_HPP

#include <iostream>

using namespace std;

const string 	usage = "usage: ./spider [options] URL\n \
	options:\n\
		-r, recursively downloads the images in the URL\n\
		-r -l [N], indicates the maximum depth level of the recursive download. Default is 5\n\
		-p [PATH], indicates the path where the downloaded files will be saved.Default: ./data";

#endif
