NAME=ft_onion

all: build run

build:
	@printf "🔨 Building image %s...\n" $(NAME)
	docker build -t $(NAME) .

run: build
	docker run --network=host --name $(NAME) $(NAME)

start:
	docker start $(NAME)

stop:    
	@docker stop $(NAME) || true

term:    
	docker exec -it $(NAME) bash
	
clean:    
	docker rm $(NAME) || true

prune:    
	docker system prune -a

re: clean build run
	
.PHONY: clean fclean stop all prune