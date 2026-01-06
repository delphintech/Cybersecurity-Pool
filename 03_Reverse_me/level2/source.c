/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:55:35 by dabouab           #+#    #+#             */
/*   Updated: 2026/01/06 16:11:29 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	no() {
	printf("Nope.");
	exit(1);
}

void	ok() {
	printf("Good job.");
	return ;
}

int	main(void) {
	int 	i;
	int		j;
	char	temp[3];
	char	buf[9];
	char	input[24];

	printf("Please enter key: ");
	if (scanf("%23s", &input[0]) != 1)
		no();
	if (input[1] != '0')
		no();
	if (input[0] != '0')
		no();
	memset(&buf[0], 0, 9);
	buf[0] = 'd';
	buf[8] = 0;
	i = 2;
	j = 1;
	while (strlen(&buf[0]) <= 8) {
		if (strlen(&input[i]) <= 2)
			break;
		temp[0] = input[i];
		temp[1] = input[i + 1];
		temp[2] = input[i + 2];
		buf[j] = atoi(&temp[0]) & 0xff;
		i += 3;
		j += 1;
	}
	if (strcmp("delabere", &buf[0]) == 0)
		ok();
	else
		no();
	return(0);
}