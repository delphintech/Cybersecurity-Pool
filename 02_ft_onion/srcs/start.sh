#!/bin/sh

# mkdir -p /var/lib/tor/hidden_service
# chown -R debian-tor:debian-tor /var/lib/tor
# chmod 700 /var/lib/tor/hidden_service
# sudo chmod 700 /var/lib/tor/hidden_service/authorized_clients

service ssh start

# tor --keygen --key-type x25519 --outfile /var/lib/tor/hidden_service/authorized_clients/dab.auth

service tor start

while [ ! -s /var/lib/tor/hidden_service/hostname ]; do
    sleep 1
done
export ONION="$(cat /var/lib/tor/hidden_service/hostname)"
# export ONION_SSH="$(cat /var/lib/tor/hidden_service/authorized_clients/dab.auth)"
echo "Tor hidden service address: $ONION"
echo "SSH access: ssh -p 4242 dab@$ONION"
# echo "Authorization key for dab: $ONION_SSH"

rm -f /etc/nginx/sites-enabled/* /etc/nginx/sites-available/* /etc/nginx/conf.d/default.conf || true

exec nginx -g 'daemon off;'

