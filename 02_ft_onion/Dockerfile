FROM	debian:bullseye

RUN		apt-get update -y && apt-get upgrade -y && apt-get install -y nginx tor torsocks curl openssh-server

COPY	./srcs/start.sh .
COPY	./srcs/nginx.conf /etc/nginx/nginx.conf
COPY	./srcs/index.html /var/www/
COPY	./srcs/torrc /etc/tor/torrc
COPY	./srcs/sshd_config /etc/ssh/sshd_config

ENTRYPOINT	["sh", "./start.sh"]