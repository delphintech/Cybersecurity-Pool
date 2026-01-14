NAME=Inquisitor

all: build run

build:
	@printf "🔨 Building image %s...\n" $(NAME)
	docker build -t $(NAME) .

run: build
	docker run --add-host host.docker.internal:host-gateway --name $(NAME) $(NAME)

start:
	docker start $(NAME)

stop:    
	@docker stop $(NAME) || true

link:
	@docker exec ft_onion cat /var/lib/tor/hidden_service/hostname

term:    
	docker exec -it $(NAME) bash
	
clean:    
	docker rm $(NAME) || true

prune:    
	docker system prune -a

re: clean build run
	
.PHONY: clean fclean stop all prune

tor:
	@docker exec ft_onion service tor restart
	Echo "TOR restarted ..."
	@MAKE link