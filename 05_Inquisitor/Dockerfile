FROM	debian:bullseye

RUN		apt-get update -y && apt-get upgrade -y && apt-get install -y \
	python3 \
	python3-dev \
	python3-pip \
	python3-venv \
	make \ 
	libpcap-dev

WORKDIR	/code

CMD ["/bin/bash", "-c", "make && tail -f /dev/null"]