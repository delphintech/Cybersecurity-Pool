# INQUISITOR
Inquisitor performs ARP poisoning in both directions (full duplex) when  active.

## Create and handle program

`make` Create environment and executable

`make clean` stop environment and delete exec

## Program usage
    ./inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>

  - `<IP-src>` The IPv4 address of the machine attacking
  - `<MAC-src>` The MAC address of the machine attacking
  - `<IP-target>` The IPv4 address of the victim machine
  - `<MAC-target>` The MAC address of the victim machine

## How to check to program

`openssl rand -hex 32` Generate a random 32 bytes hexadecimal key (1 bytes = 2 characters)

`oathtool –totp $(cat key.txt)` Generate code based on the given key (not encrypted)