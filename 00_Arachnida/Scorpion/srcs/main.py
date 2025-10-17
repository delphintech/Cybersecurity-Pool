#!/usr/bin/env python3
import sys
import utils

def main():
	args = sys.argv[1:]
	if not args:
		print(utils.USAGE)
		sys.exit(1)


# Laumch main only if called directly
if __name__ == "__main__":
    main()