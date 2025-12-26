/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/18 15:55:40 by dabouab           #+#    #+#             */
/*   Updated: 2025/12/26 18:25:33 by dabouab          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


// The function takes a parameter ????? 
void	___syscall_malloc(void) {
	printf("Nope.");
	exit(1);
}


int	main(void) {
	int		i;
	int		j;
	int		comp;
	char	buf[9];
	char	temp[3];
	char	input[24];

	printf("Please enter key: ");
	if (scanf("%23s", &input[0]) == 1) {
		if (input[1] == "2") {
			if (input[0] == "4") {
				memset(&buf[0], 0 , 9);
				buf[0] = "*";
				buf[9] = 0;
				i = 2; 
				j = 1;
				while (strlen(&buf[0]) < 8) {
					if (strlen(&input[0] < i))
						break ;
					temp[0] = input[i];
					temp[1] = input[i + 1];
					temp[2] = input[i + 2];
					buf[j] = atoi(&temp[0]) & 0xff;
					i += 3;
					j += 1;
				}
				comp = strcmp("********", &buf[0]);
				c
			} else
				___syscall_malloc();
		} else 
			___syscall_malloc();
	} else
		___syscall_malloc();
}