NAME=ft_onion
TEST=test

COLOR = \e[1;34m
RESET = \e[0m

all: build run info

build:
	@printf "🔨 Building image %s...\n" $(NAME)
	@docker build -t $(NAME) .

run: build
	@docker run --name $(NAME) $(NAME)

start:
	@docker start $(NAME)

stop:    
	@docker stop $(NAME) || true

info:
	@ONION=$$(docker exec ft_onion cat /var/lib/tor/hidden_service/hostname); \
	printf "\n$(COLOR)Tor hidden service address:\n  $(RESET)$$ONION\n"; \
	printf "$(COLOR)Test standard localhost (inside container):\n  $(RESET)curl localhost:80\n"; \
	printf "$(COLOR)Test tor (inside container):\n  $(RESET)curl --socks5-hostname localhost:9052 http://$$ONION\n"; \
	printf "$(COLOR)SSH access (inside container):\n  $(RESET)ssh -p 4242 dab@localhost\n"

term:    
	@docker exec -it $(NAME) bash
	
clean:  
	@docker rm $(NAME) || true

prune:    
	@docker system prune -a

re: clean build run
	
.PHONY: clean fclean stop all prune

tor:
	@docker exec ft_onion service tor restart
	@echo "TOR restarted ..."
	@MAKE link