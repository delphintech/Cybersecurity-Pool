import os
from termcolor import cprint
from PIL import Image
from PIL.ExifTags import TAGS

USAGE = "usage: ./scorpion FILE1 [FILE2 ...]\n"

def check_img(file: str) -> bool:
	exts = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

	for x in exts:
		if file.endswith(x):
			if os.access(file, os.R_OK):
				return True
	return False

def	meta(file: str):
	meta = {}
	image = Image.open(file)
	cprint(f"---------- {image.filename} ----------", "blue", "on_white")
	print(f"Size: {image.size}")
	print(f"Dimension: {image.height} x {image.width}")
	print(f"Format: {image.format}\n")
	exifdata = image.getexif()
	if not exifdata:
		cprint("This image has no EXIF", "black", "on_white")
		image.close()
		return
	cprint("EXIF:", "black", "on_white")
	for tag_id in exifdata:
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)
		if isinstance(data, bytes):
			data = data.decode()
		print(f"{tag}: {data}")
	image.close()
	


# def display_meta(meta: dict):
# 	print("")