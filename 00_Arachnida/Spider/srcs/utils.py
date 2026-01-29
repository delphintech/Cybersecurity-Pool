from urllib.parse import urlparse
import os

USAGE = "usage: ./spider [options] URL\n \
	options:\n\
		-r, recursively downloads the images in the URL\n\
		-r -l [N], indicates the maximum depth level of the recursive download. Default is 5\n\
		-p [PATH], indicates the path where the downloaded files will be saved.Default: ./data"

def get_img_name(url):
	exts = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
	is_img = False

	if not url:
		return ""

	parsed = urlparse(url)
	name = os.path.basename(parsed.path)
	for x in exts:
		if name.endswith(x):
			is_img = True
	if not is_img:
		return ""
	
	if len(name) > 50:
		name = name[-50:]
	return name