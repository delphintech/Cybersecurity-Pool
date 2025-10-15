#ifndef SPIDER_HPP
#define SPIDER_HPP

#include "utils.hpp"

class Spider {
private:
	string			url;
	string			path;
	vector<string>	done;
	int				depth;

public:
	Spider(int ac, char **av);
	~Spider();

	const string	get_url() const;

	void		check(string opt);
	void		scrap(const string url);
	void		download_img(const string url);
};

#endif
