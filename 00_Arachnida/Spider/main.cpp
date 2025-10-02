/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 11:39:00 by dabouab           #+#    #+#             */
/*   Updated: 2025/10/02 12:49:11 by dabouab          ###   ########.fr       */
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
	} catch (exception e) {
		cerr << e.what() << "\n\n" << USAGE << endl;
		return (EXIT_FAILURE);
	}
}