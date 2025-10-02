#include <iostream>
#include "Spider.hpp"

Spider::Spider(int ac, char **av) : path("./data/"), depth(0) {
	string	opt;
	string	arg;

	for (int i = 1; i <= ac; i++) {
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
			if (i != ac)
				throw invalid_argument("URL should be last");
			url = av[i];
		}
	}
}

Spider::~Spider() {
}

void	Spider::check(string opt) {
	if (opt.find("l") != string::npos && opt.find("r") == string::npos)
		throw invalid_argument("Depth option without recursive");
	if (opt.find("l") != string::npos && (depth < 0 || depth > 1000))
		throw invalid_argument("Invalid depth (must be between 0 and 1000)");
	// TODO: check path valid, exist, correct rights or create it
	// TODO: check if URL valid ?
}