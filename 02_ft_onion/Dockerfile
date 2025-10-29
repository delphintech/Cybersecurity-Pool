FROM	debian:bullseye

RUN		apt-get update -y && apt-get upgrade -y && apt-get install -y nginx tor curl

COPY	./srcs/nginx.conf /etc/nginx/nginx.conf
COPY	./srcs/index.html /var/www/
COPY	./srcs/torrc /etc/tor/torrc

RUN		service tor start

# Launch nginx
CMD ["nginx", "-g", "daemon off;"]