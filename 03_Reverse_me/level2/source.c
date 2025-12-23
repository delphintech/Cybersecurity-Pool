/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:55:35 by dabouab           #+#    #+#             */
/*   Updated: 2025/12/23 18:05:23 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

void	no() {
	printf("Nope.");
	exit(1);
}

void	ok() {
	printf("Good job.");
	exit(0);
}

int	main(void) {
	char	input[32];
	char	buf[9]
	int 	ret;

	printf("Please enter key: ");
	if (scanf("%s", &input[0]) == 1) {
		if (input[1] == '0')
			if (input[0] == '0')
				memset(buf, 0, 9);
				buf[0] = "d"
				if (strlen(&buf[0]) >= 8)
				else
					
			else 
				no();
		else
			no();
	} else 
		no();
}


// strlen(&input[0]);

// atoi($input[0]);

// strmcp("delabere", );

// 0012345678delabere

// ebp-0x40 ""
// 0xc

// ecx = "0"
// ebp-0x35 = argument
// ebx-0xc = "@ ."




// eax = 64  ("@")
// eax = 32  (" ")
// eax = -120

// "%23s"


// strlen("d")