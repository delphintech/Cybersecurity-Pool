#!/usr/bin/env python3
import sys
import utils
from termcolor import cprint

def main():
	args = sys.argv[1:]
	if not args:
		print(utils.USAGE)
		sys.exit(1)
	
	i = 0
	while i < len(args):
		if utils.check_img(args[i]):
			utils.meta(args[i])
		else:
			cprint(f"'{args[i]}' is not an image or is not readable", "red")
		if (i < len(args) - 1):
			print("\n\n")
		i += 1


# Laumch main only if called directly
if __name__ == "__main__":
    main()