from netaddr import EUI, IPAddress

class Inquisitor:
	usage="./inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>\n\n\
	- <IP-src> The IPv4 address of the machine attacking\n\
	- <MAC-src> The MAC address of the machine attacking\n\
	- <IP-target> The IPv4 address of the victim machine\n\
	- <MAC-target> The MAC address of the victim machine\n"

	def __init__(self, args):
		try:
			self.src_ip = IPAddress(args[0])
			self.src_mac = EUI(args[1])
			self.target_ip = IPAddress(args[2])
			self.target_mac = EUI(args[3])

			if self.src_ip.version != 4 or self.target_ip.version != 4:
				raise ValueError("Only Ipv4 is accepted\n")
		except Exception as e:
			print(str(e) + "\n" + self.usage)
		
	def __str__(self):
		return(f"Inquisitor:\n"
			f"  - Attacker: {str(self.src_ip)}  | {str(self.src_mac)}\n"
			f"  - Victim:   {str(self.target_ip)}  | {str(self.target_mac)}\n")