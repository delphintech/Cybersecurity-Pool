#!/usr/bin/env python3
import sys
# import spider
# import utils

def main():
    print(f"COucou {sys.argv[1]}")
    # Récupération des arguments
    # args = sys.argv[1:]  # sys.argv[0] est le nom du script
    # if len(args) < 2:
    #     print(utils.USAGE)
    #     sys.exit(1)

    # spider	spider

# Laumch main only if called directly
if __name__ == "__main__":
    main()


# int	main(int ac, char **av) {
# 	if (ac < 2) {
# 		cerr << "No argument\n\n" << USAGE << endl;
# 		return (EXIT_FAILURE);
# 	}
	
# 	try {
# 		Spider	spider(ac, av);
		
# 		spider.scrap(spider.get_url());
# 	} catch ( invalid_argument &e) {
# 		cerr << e.what() << "\n\n" << USAGE << endl;
# 		return (EXIT_FAILURE);
# 	} catch (const exception &e) {
# 		cerr << e.what() << "\n" << endl;
# 		return (EXIT_FAILURE);
# 	}
# }