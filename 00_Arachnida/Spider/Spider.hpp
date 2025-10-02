#ifndef SPIDER_HPP
#define SPIDER_HPP

#include <iostream>
#include "curl/curl.h"
#include <libxml/HTMLparser.h>

using namespace std;

#define	USAGE "usage: ./spider [options] URL\n \
	options:\n\
		-r, recursively downloads the images in the URL\n\
		-r -l [N], indicates the maximum depth level of the recursive download. Default is 5\n\
		-p [PATH], indicates the path where the downloaded files will be saved.Default: ./data"

class Spider
{
private:
	string	url;
	string	path;
	int		depth;

public:
	Spider(int ac, char **av);
	~Spider();

	void	check(string opt);
};

#endif
