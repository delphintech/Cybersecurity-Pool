#!/bin/sh

mkdir -p /etc/tor/hidden_service
chown -R debian-tor:debian-tor /etc/tor/hidden_service
chmod 700 /etc/tor/hidden_service

service ssh start

service tor start
while [ ! -s /etc/tor/hidden_service/hostname ]; do
    sleep 1
done
export ONION="$(cat /etc/tor/hidden_service/hostname)"
echo "Tor hidden service address: $ONION"

rm -f /etc/nginx/sites-enabled/* /etc/nginx/sites-available/* /etc/nginx/conf.d/default.conf || true

exec nginx -g 'daemon off;'

