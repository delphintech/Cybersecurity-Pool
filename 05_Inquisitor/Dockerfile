FROM	debian:bullseye

RUN		apt-get update -y && apt-get upgrade -y && apt-get install -y \
			python \
			make

COPY	./code .
WORKDIR	/code

ENTRYPOINT	["sh", "make"] 