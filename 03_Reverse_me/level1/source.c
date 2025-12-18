/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:41:38 by dabouab           #+#    #+#             */
/*   Updated: 2025/12/18 18:09:31 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

int	main(void) {
	char *pwd = "__stack_check";
	char buf[24];
	
	printf("Please enter key: ");
	scanf("%s", &buf[0]);
	if (strcmp(pwd, buf) == 0) {
		printf("Good job.\n");
	} else {
		printf("Nope.\n");
	}
}
