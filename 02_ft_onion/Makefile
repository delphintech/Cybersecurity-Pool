NAME=ft_onion

all: $(NAME)

$(NAME):    
	docker build -t $(NAME) .
	docker run -it --name $(NAME)
	
stop:    
	docker stop $(NAME)
	
term:    
	docker exec -it $(NAME) bash
	
stop:    
	docker stop $(NAME)
	
clean:    
	docker rm $(NAME)
	
prune:    
	docker system prune -a
	
.PHONY: clean fclean stop all prune