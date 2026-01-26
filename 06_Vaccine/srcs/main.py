#!/usr/bin/env python3
import sys
from vaccine import Vaccine

def main():
    args = sys.argv[1:]
    if not args:
        print(Vaccine.usage)
        sys.exit(1)

    try:

    except Exception as e:
        print(e)


# Laumch main only if called directly
if __name__ == "__main__":
    main()
