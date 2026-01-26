#!/usr/bin/env python3
from stockholm import Stockholm
import sys


def main():
    args = sys.argv[1:]

    try:
        stockholm = Stockholm(args)
        if "h" in stockholm.options:
            Stockholm.help()
        elif "v" in stockholm.options:
            Stockholm.version()
        elif "r" in stockholm.options:
            stockholm.decrypt()
        elif "k" in stockholm.options:
            if stockholm.key:
                stockholm.decrypt_key()
            else:
                Stockholm.generate_key()
        else:
            stockholm.encrypt()
    except ValueError as e:
        print(f"{e}\n\n{Stockholm.usage}")

    except Exception as e:
        print(e)


# Laumch main only if called directly
if __name__ == "__main__":
    main()
