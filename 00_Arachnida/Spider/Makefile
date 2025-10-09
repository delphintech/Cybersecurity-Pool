# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dabouab <dabouab@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/09 12:54:37 by dabouab           #+#    #+#              #
#    Updated: 2025/10/09 14:14:56 by dabouab          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME=spider

all: $(NAME)

$(NAME):
	docker build -t spider .
	docker run -it --name spider -v "$(PWD)/srcs":/srcs spider

stop:
	docker stop spider

term:
	docker exec -it spider bash

clean:
	docker run --rm -v "$(PWD)/srcs":/srcs -w /srcs spider make clean
	docker stop spider

fclean: clean
	docker rm spider

prune:
	docker system prune -a

.PHONY: clean fclean stop all prune