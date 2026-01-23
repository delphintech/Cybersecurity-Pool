NAME=inquisitor

all: build run term

build:
	@printf "🔨 Building image %s...\n" $(NAME)
	@docker build -t $(NAME) .

run: build
	@docker run --cap-add=NET_RAW --network=host -it --name $(NAME) -d -v "$(PWD)/code":/code $(NAME)

start:
	@docker start $(NAME)

stop:   
	@docker exec $(NAME) bash -c "cd /code && make clean" 2>/dev/null || true
	@docker stop $(NAME) 2>/dev/null || true

term:    
	@docker exec -it $(NAME) bash
	
clean: stop
	@docker rm $(NAME) || true

prune:    
	@docker system prune -a

re: clean build run
	
.PHONY: clean fclean stop all prune