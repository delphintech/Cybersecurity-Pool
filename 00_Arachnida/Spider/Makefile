# Compiler
COMP = c++ -g -Werror -Wall -Wextra -MMD

# Nom du programme
NAME = spider

# Couleur
COLOR = \e[1;32m
RESET = \e[0m

# Liste des sources
SRCS += Spider.cpp, main.cpp

# Liste des ojets
OBJS = $(SRCS:.cpp=.o)

# Liste des dependences 
DEPS = $(SRCS:.cpp=.d)

all	:
	$(NAME)
		
# Compile les objects avec les flags
%.o: %.c
	@$(COMP) -c $< -o $@

$(NAME)	:	$(OBJS)
	@$(COMP) -o $(NAME) $(OBJS)
	@printf $COLOR
	@printf "  _____ .___  _ .___   .____  .___\n"
	@printf " (      /   \ | /   `  /      /   \\n"
	@printf "  `--.  |,_-' | |    | |__.   |__-'\n"
	@printf "     |  |     | |    | |      |  \ \n"
	@printf "\___.'  /     / /---/  /----/ /   \\n"
	@printf $RESET

clean	:                 
	@rm -f $(OBJS)
	@printf "Objects deleted ... ❌"

fclean	:	clean
	@rm -f $(NAME)
	@printf "Exec deleted ...... ❌"

re	:	fclean all

.PHONY: all clean fclean re

# Inclue les dependences (⚠ add -MMD to compile)
-include $(DEPS)