#!/usr/bin/env python3
import sys
from spider import Spider
import utils

def main():
	args = sys.argv[1:]
	if not args:
		print(utils.USAGE)
		sys.exit(1)

	try:
		spider = Spider(args)
		spider.scrap(spider.url, spider.depth)
		print(f"📥 {Spider.imgs} images downloaded")
	except ValueError as e:
		print(f"{e}\n\n{utils.USAGE}")
		
	except Exception as e:
		print(e)

# Laumch main only if called directly
if __name__ == "__main__":
    main()