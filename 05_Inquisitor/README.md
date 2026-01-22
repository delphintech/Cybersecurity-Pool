# INQUISITOR
Inquisitor performs ARP poisoning in both directions (full duplex) when  active.

## Setup

`make` Create docker, activate the python environnement, create the executable and launch the docker terminal

`make clean` Stop docker, clean environment delete exec and docker image

## Usage
    sudo ./inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>

  - `<IP-src>` The IPv4 address of the machine (or gateaway) we want to replace
  - `<MAC-src>` The MAC address of the machine (or gateaway) we want to replace
  - `<IP-target>` The IPv4 address of the victim machine
  - `<MAC-target>` The MAC address of the victim machine

## Test

`openssl rand -hex 32` Generate a random 32 bytes hexadecimal key (1 bytes = 2 characters)

`oathtool –totp $(cat key.txt)` Generate code based on the given key (not encrypted)