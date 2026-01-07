#!/usr/bin/env python3
import utils
import Stockholm
import sys

def main():
	args = sys.argv[1:]
	if not args:
		print(utils.USAGE)
		sys.exit(1)
	
	try:
		stockholm = Stockholm(args)
	except ValueError as e:
		print(f"{e}\n\n{utils.USAGE}")
		
	except Exception as e:
		print(e)

# Laumch main only if called directly
if __name__ == "__main__":
    main()