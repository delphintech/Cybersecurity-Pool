import os
import urllib
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Vaccine:
    usage = "Usage: ./vaccine [-oX] URL\n \
    options:\n\
        * -o <file_name>: Archive file, if not specified it will be stored in a default one\n \
        * -X <GET|POST>: Type of request, if not specified GET will be used.\n\
        * -d <max_depth>` Maximun crawl depth. 3 by default, maximum 10\n"

    def __init__(self, args):
        self.archive = ""
        self.request = "GET"
        self.max_depth = 3

        i = 0
        while i < len(args):
            if (args[i][0] == '-'):
                if len(args[i]) < 2:
                    raise ValueError("Bad option call")
                
                match args[i][1]:
                    case 'o':
                        i += 1
                        self.archive = args[i]
                    case 'X':
                        i += 1
                        self.request = args[i].upper()
                    case 'd':
                        i += 1
                        self.request = args[i]
                    case _:
                        raise ValueError("Wrong option")
            else:
                if i < len(args) - 1:
                    raise ValueError("URL should be last")
                self.url = args[i]
            i += 1
            self.check_args()
            self.init_session()

    def check_args(self):
        # Check if valid request
        if self.request != "GET" or self.request != "POST":
            raise ValueError("Request must be GET or POST")
        # check max depth validity
        if self.depth < 0 or self.depth > 10:
            raise ValueError("Crawling depth must be between 0 and 10")
        # Check for valid url
		parsed = urlparse(self.url)
		if not parsed.scheme or not parsed.netloc:
			raise ValueError("Invalid url")
        # check archive file is valid
        if len(self.archive) > 100:
            raise ValueError("File name must be less than 100 character")
        if os.access(self.archive, F_OK) and not os.access(self.archive, W_OK):
            raise ValueError("File already exists and lack permission's access")
    
    def init_session(self):
        ''' create session '''
		options = Options()
		options.add_argument("--headless")
		self.driver = webdriver.Chrome(options=options)
    
    def __str__(self):
        return (f"Vaccine:\n  * URL:      {self.url}\n\
  * Request:  {self.request}\n * Archive:  {self.archive}")

  	def __del__(self):
		driver = getattr(self, "driver", None)
		if driver:
			driver.quit()


#   def check(self, opt):
# 		''' Check for option validity '''
# 		if 'l' in opt and 'r' not in opt:
# 			raise ValueError("Depth option without recursive")
# 		if 'l' in opt and (self.depth < 0 or self.depth > 10):
# 			raise ValueError("Invalid depth (must be between 0 and 10)")
		
# 		''' Check for folder path '''
# 		if os.path.isdir(self.path):
# 			shutil.rmtree(self.path)
# 		os.makedirs(self.path)
# 		if self.path[-1] != '/':
# 			self.path += "/"

# 		''' Check for valid url '''
# 		parsed = urlparse(self.url)
# 		if not parsed.scheme or not parsed.netloc:
# 			raise ValueError("Invalid url")

# 	def scrap(self, url, depth=0):
# 		elements = []
# 		links = []

# 		if url in self.done:
# 			return

# 		print(f"Downloading images from: {url} (depth: {self.depth - depth}) ...\n")

# 		''' Get the page content '''
# 		self.driver.get(url)
# 		WebDriverWait(self.driver, 5).until(
#             lambda d: d.execute_script("return document.readyState") == "complete"
#         )
# 		if not self.driver.current_url:
# 			return

# 		''' Parse and store each image url '''
# 		elements = self.driver.find_elements(By.TAG_NAME, "img")
# 		links = [e.get_attribute("src") for e in elements]

# 		''' Download each images '''
# 		headers = {
#             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36",
#             "Referer": url,
#         }
# 		for x in links:
# 			filename = utils.get_img_name(x)
# 			if not filename or x == None:
# 				continue
# 			filepath = self.path + filename
# 			img_url = urllib.parse.urljoin(url, x)
# 			with open(filepath, 'wb') as file:
# 				file.write(requests.get(img_url, headers=headers).content)
# 				Spider.imgs += 1

# 		self.done.append(url)
# 		elements.clear()
# 		links.clear()

# 		''' Scrap all the links in the page '''
# 		if depth > 0:
# 			elements = self.driver.find_elements(By.TAG_NAME, "a")
# 			links = [e.get_attribute("href") for e in elements]
# 			for x in links:
# 				if x != None and not x.startswith("#") and not x.startswith("mailto:") \
# 					and not x.startswith("javascript"):
# 					link_url = urllib.parse.urljoin(self.url, x)
# 					self.scrap(link_url, depth - 1)

