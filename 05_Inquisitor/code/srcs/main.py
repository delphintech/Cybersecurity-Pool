#!/usr/bin/env python3
import sys
from inquisitor import Inquisitor

def main():
	args = sys.argv[1:]
	if not args:
		print(Inquisitor.usage)
		sys.exit(1)

	try:
		inquisitor = Inquisitor(args)
		print(inquisitor)
		# libpcap (capture) →  sniff ARP packets
		# raw socket (send) → craft + inject Ethernet/ARP frames
		# timer loop → keep poisoning alive
		# Handle Ctrl + C signal to restore the correct tables
	except Exception as e:
		print(e)

# Laumch main only if called directly
if __name__ == "__main__":
    main()