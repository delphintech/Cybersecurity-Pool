#!/usr/bin/env python3
import sys
import utils

def main():
	args = sys.argv[1:]
	if args != 2:
		print("Wrong number of arguments\n\n"  + utils.USAGE)
		sys.exit(1)
	
	if args[0] == "-g":
		if not utils.is_valid_hexa_key(args[1]):
			print("The given key must be heaxdecimal and be between 64 and 72 characters.\n\n" + utils.USAGE)
			sys.exit(1)
		utils.store_key(args[1])
	elif args[0] == "-k":
		key = utils.decrypt_key(args[1])
		if key:
			utils.generate_pwd(key)
	else:
		print("Invalid arguments\n\n" + utils.USAGE)



# Laumch main only if called directly
if __name__ == "__main__":
    main()