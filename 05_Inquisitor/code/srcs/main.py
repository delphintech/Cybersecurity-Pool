#!/usr/bin/env python3
import sys
from inquisitor import Inquisitor
import utils

def main():
	args = sys.argv[1:]
	if not args:
		print(Inquisitor.usage)
		sys.exit(1)

	try:
		inquisitor = Inquisitor(args)
		print(inquisitor)
	except ValueError as e:
		print(f"{e}\n\n{Inquisitor.usage}")
		
	except Exception as e:
		print(e)

# Laumch main only if called directly
if __name__ == "__main__":
    main()