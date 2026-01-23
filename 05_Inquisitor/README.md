# INQUISITOR
Inquisitor performs ARP poisoning between a FTP server and a machine, in both directions (full duplex).\
It catches the files exchanged during its runtime and display their name.\
The ARP tales a restored when the program is stopped.

## Setup

`make` Create docker, activate the python environnement, create the executable and launch the docker terminal: \
`make` inside the docker terminal create the executable


`make clean` Stop docker, clean environment delete exec and docker image

## Usage
    ./inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>

  ⚠️ This program require root permission 

  - `<IP-src>` The IPv4 address of the machine (or gateaway) we want to replace
  - `<MAC-src>` The MAC address of the machine (or gateaway) we want to replace
  - `<IP-target>` The IPv4 address of the victim machine
  - `<MAC-target>` The MAC address of the victim machine

## Test

**Check the ARP tables**\
`arp -n` 

**Create a FTP server**\
`sudo apt install vsftpd`\
`sudo service vsftpd start`

**FTP Exchange**\
`ftp <ftp_server_ip>` Connect\
`put <file_name>` Upload\
`get <file_name>` Download

