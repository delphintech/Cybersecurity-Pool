#!/bin/sh

service ssh start
service tor start

while [ ! -s /var/lib/tor/hidden_service/hostname ]; do
    sleep 1
done

rm -f /etc/nginx/sites-enabled/* /etc/nginx/sites-available/* /etc/nginx/conf.d/default.conf || true

exec nginx -g 'daemon off;'

