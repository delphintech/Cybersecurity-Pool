/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:55:35 by dabouab           #+#    #+#             */
/*   Updated: 2025/12/26 16:04:47 by dabouab          ###   ########.fr       */
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
	exit(0);
}

int	main(void) {
	char	input[24];
	char	buf[9];
	char	temp[3];
	int 	i;
	int		j;

	printf("Please enter key: ");
	if (scanf("%23s", &input[0]) == 1) {
		if (input[1] == '0')  {
			if (input[0] == '0') {
				memset(buf, 0, 9);
				buf[0] = 'd';
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
				no();
			} else
				no();
		} else 
			no();
	} else 
		no();
}