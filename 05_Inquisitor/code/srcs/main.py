#!/usr/bin/env python3
import sys
import time
from inquisitor import Inquisitor


def main():
    args = sys.argv[1:]
    if not args:
        print(Inquisitor.usage)
        sys.exit(1)

    try:
        inquisitor = Inquisitor(args)
        inquisitor.connect()
        print ('[x] Ongoing ARP poisoning ... Ctrl+C to stop\n\n')

        while True:
            inquisitor.poison()
            inquisitor.intercept()

            time.sleep(1)

    except KeyboardInterrupt:
        print("[!] Program interrupted !\n Restoring the network, please wait...")
        inquisitor.restore()

    except Exception as e:
        print(e)


# Laumch main only if called directly
if __name__ == "__main__":
    main()
