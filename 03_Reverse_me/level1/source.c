/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:41:38 by dabouab           #+#    #+#             */
/*   Updated: 2025/12/26 15:40:07 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

int	main(void) {
	char *pwd = "__stack_check";
	char input[32];
	
	printf("Please enter key: ");
	scanf("%s", &input[0]);
	if (strcmp(pwd, input) == 0)
		printf("Good job.\n");
	else
		printf("Nope.\n");
	return (0);
}