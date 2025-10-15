# Compiler
COMP = c++ -g -Werror -Wall -Wextra -I/usr/include/libxml2

# Librairies
LIBS = -lcurl -lxml2

# Nom du programme
NAME = spider

# Couleur
COLOR = \e[1;31m
RESET = \e[0m

# Liste des sources
SRCS += Spider.cpp utils.cpp main.cpp

# Liste des ojets
OBJS = $(SRCS:.cpp=.o)

all	: $(NAME)

# Compile les objects avec les flags
%.o: %.cpp
	@$(COMP) -c $< -o $@

$(NAME)	:	$(OBJS)
	@$(COMP) -o $(NAME) $(OBJS) $(LIBS)
	@printf "$(COLOR)"
	@printf "  _____ .___  _ .___   .____  .___\n"
	@printf " (      /   \\ | /   \`  /      /   \\ \n"
	@printf "  \`--.  |,_-' | |    | |__.   |__-'\n"
	@printf "     |  |     | |    | |      |  \\\\ \n"
	@printf "\\\___.'  /     / /---/  /----/ /   \\ \n"
	@printf "$(RESET)"

clean	:                 
	@rm -f $(OBJS)
	@printf "Objects deleted ... ❌\n"

fclean	:	clean
	@rm -f $(NAME)
	@printf "Exec deleted ...... ❌\n"

re	:	fclean all

.PHONY: all clean fclean re

test:
	./spider https://www.scrapingcourse.com/pagination