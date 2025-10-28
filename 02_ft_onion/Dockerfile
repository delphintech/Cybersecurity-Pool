FROM	debian:bullseye

RUN		apt-get update -y && apt-get upgrade -y && apt-get install -y nginx tor

COPY	./srcs/nginx.conf /etc/nginx/nginx.conf
COPY	./srcs/index.html /www/

# Create a certificate
RUN		mkdir -p /etc/nginx/ssl
RUN		openssl req -x509 -nodes -out /etc/nginx/ssl/inception.crt -keyout /etc/nginx/ssl/inception.key \
	-subj "/C=FR/ST=IDF/L=Paris/O=42/OU=42/CN=login.42.fr/UID=login"

# Expose le port sp"ecifique et le rend disponible pour la communication entre conteneurs
EXPOSE		443

# Launch nginx
CMD ["nginx", "-g", "daemon off;"]