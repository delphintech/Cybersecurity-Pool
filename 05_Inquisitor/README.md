To be able to connect via ssh:

in ~/.ssh/config:

	Host *.onion *-tor
    ProxyCommand ncat --proxy-type socks5 --proxy 127.0.0.1:9052 %h %p
    CheckHostIP no
    Compression yes
    Protocol 2

to test with curl:

 curl --socks5-hostname localhost:9050 http://<onion_name>.onion