from netaddr import EUI, IPAddress
import socket


class Inquisitor:
    usage = "./inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>\n\n\
    - <IP-src> The IPv4 address of the machine attacking\n\
    - <MAC-src> The MAC address of the machine attacking\n\
    - <IP-target> The IPv4 address of the victim machine\n\
    - <MAC-target> The MAC address of the victim machine\n"

    def __init__(self, args):
        try:
            self.src_ip = IPAddress(args[0])
            self.src_mac = EUI(args[1])
            self.tg_ip = IPAddress(args[2])
            self.tg_mac = EUI(args[3])

            with open("/sys/class/net/eth0/address", "r") as f:
                my_mac = f.read().strip()
            self.my_mac = EUI(my_mac)

            if self.src_ip.version != 4 or self.tg_ip.version != 4:
                raise ValueError("Only Ipv4 is accepted\n")
        except Exception as e:
            print(str(e) + "\n" + self.usage)

    @staticmethod
    def create_ARP_packet(ip, mac):
        """
        Return an ARP packet response 
        """
        # source_mac = binascii.unhexlify('00:A0:C9:14:C8:29'.replace(':', ''))
        # #b'\x00\x00\x00\x00\x00\x00' sender mac address
        # dest_mac = binascii.unhexlify('ff:ff:ff:ff:ff:ff'.replace(':', ''))
        # #  b'\xff\xff\xff\xff\xff\xff'  target mac address

        # source_ip = "192.168.100.3"  # sender ip address
        # dest_ip = "192.168.100.1"  # target ip address

        # Ethernet Header
        protocol = 0x0806  # 0x0806 for ARP
        eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, protocol)

        # # ARP header
        # htype = 1  # Hardware_type ethernet
        # ptype = 0x0800  # Protocol type TCP
        # hlen = 6  # Hardware address Len
        # plen = 4  # Protocol addr. len
        # operation = 1  # 1=request/2=reply
        # src_ip = socket.inet_aton(source_ip)
        # dst_ip = socket.inet_aton(dest_ip)
        # arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation,
        #                     source_mac, src_ip, dest_mac, dst_ip)

        # packet = eth_hdr + arp_hdr

    def connect(self):
        """
        Enables IP route ( IP Forward ) in linux-based distro
        """
        with open("/proc/sys/net/ipv4/ip_forward", "rw") as f:
            if f.read() == 1:
                return
            f.write(1)

        # Convert ETHERTYPE_ARP to network byte order for the socket call
        ARP_PROTOCOL = socket.htons(socket.ETHERTYPE_ARP)
        # socket is a raw socket that will ONLY receive/send ARP packets
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, ARP_PROTOCOL)
        self.socket.bind(("wlp5s0", 0))

    def poison(self):
        """
        Send ARP response to src and target with attacker MAC
        """

    def intercept(self):
        """
        Intercept the packets and display file name
        """

    def restore(self):
        """
        Send the ARP response with correct addresses to restore the ARP tables
        """

        # Close the socket if it exists
        self.socket and self.socket.close()

    def __str__(self):
        return (f"Inquisitor:\n"
                f"  - Attacker:   {str(self.my_mac)}\n"
                f"  - Source: {str(self.src_ip)}  | {str(self.src_mac)}\n"
                f"  - Victim:   {str(self.tg_ip)}  | {str(self.tg_mac)}\n")
