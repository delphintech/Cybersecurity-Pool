/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:55:40 by dabouab           #+#    #+#             */
/*   Updated: 2026/01/06 16:34:00 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	___syscall_malloc(void) {
	printf("Nope.");
	exit(1);
}

void	____syscall_malloc(void) {
	printf("Good job.");
}


int	main(void) {
	int		i;
	int		j;
	int		comp;
	char	buf[9];
	char	temp[3];
	char	input[24];

	printf("Please enter key: ");
	if (scanf("%23s", &input[0]) != 1)
		___syscall_malloc();
	if (input[1] != '2')
		___syscall_malloc();
	if (input[0] != '4')
		___syscall_malloc();
	memset(&buf[0], 0 , 9);
	buf[0] = '*';
	buf[8] = 0;
	i = 2; 
	j = 1;
	while (strlen(&buf[0]) < 8) {
		if ((int)strlen(&input[0]) < i)
			break ;
		temp[0] = input[i];
		temp[1] = input[i + 1];
		temp[2] = input[i + 2];
		buf[j] = atoi(&temp[0]) & 0xff;
		i += 3;
		j += 1;
	}
	comp = strcmp("********", &buf[0]);
	if (comp - -2 == 0)
		___syscall_malloc();
	else if (comp - -1 == 0)
		___syscall_malloc();
	else if (comp == 0)
		____syscall_malloc(); // ✅
	else if (comp - 1 == 0)
		___syscall_malloc();
	else if (comp - 3 == 0)
		___syscall_malloc();
	else if (comp - 4 == 0)
		___syscall_malloc();
	else if (comp - 5 == 0)
		___syscall_malloc();
	else if (comp - 73 == 0)
		___syscall_malloc();
	else
		___syscall_malloc();

	return (0);
}