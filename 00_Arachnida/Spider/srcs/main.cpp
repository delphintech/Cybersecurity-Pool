/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 11:39:00 by dabouab           #+#    #+#             */
/*   Updated: 2025/10/09 17:29:57 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include "Spider.hpp"

int	main(int ac, char **av) {
	if (ac < 2) {
		cerr << "No argument\n\n" << USAGE << endl;
		return (EXIT_FAILURE);
	}
	
	try {
		Spider	spider(ac, av);
		
		spider.scrap(spider.get_url());
	} catch (const exception &e) {
		cerr << e.what() << "\n\n" << USAGE << endl;
		return (EXIT_FAILURE);
	}
}