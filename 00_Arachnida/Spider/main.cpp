/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 11:39:00 by dabouab           #+#    #+#             */
/*   Updated: 2025/10/02 11:49:31 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include "Spider.hpp"

void	error(string s) {
	cerr << s << endl;
	exit(EXIT_FAILURE);
}

int	main(int ac, char **av) {
	string	url;
	string	path = "./data";
	int		level = -1;

	if (ac < 2)
		error("No argument\n\n" USAGE);
}