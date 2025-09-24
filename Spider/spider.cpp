#include <iostream>

using namespace std;

#define	USAGE "usage: ./spider [options] URL\n \
	options:\n\
		-r, recursively downloads the images in the URL\n\
		-r -l [N], indicates the maximum depth level of the recursive download. Default is 5\n\
		-p [PATH], indicates the path where the downloaded files will be saved.Default: ./data"

void	error(string s) {
	cerr << s << endl;
	exit(EXIT_FAILURE);
}

void	scrap(string url, int level, string path) {

}

int	main(int ac, char **av) {
	string	url;
	string	path = "./data";
	int		level = -1;

	if (ac < 2)
		error("No argument\n\n" USAGE);


}
