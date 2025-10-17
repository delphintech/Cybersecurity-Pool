import os
import requests
from bs4 import BeautifulSoup
import utils
import urllib.parse

class Spider:
	imgs = 0

	def __init__(self, args):
		self.url = ""
		self.path = "./data/"
		self.depth = 0
		self.done = []

		opt = ""
		i = 0
		while i < len(args):
			if (args[i][0] == '-'):
				if len(args[i]) < 2:
					raise ValueError("Bad option call")
				
				match args[i][1]:
					case 'r':
						if 'r' in opt:
							raise ValueError("Duplication option r")
						opt += "r"
						if 'l' not in opt:
							self.depth = 5
					case 'l':
						if 'l' in opt:
							raise ValueError("Duplication option l")
						opt += "l"
						i += 1
						self.depth = int(args[i])
					case 'p':
						if 'p' in opt:
							raise ValueError("Duplication option p")
						opt += "p"
						i += 1
						self.path = args[i]
					case _:
						raise ValueError("Wrong option")
			else:
				if i < len(args) - 1:
					raise ValueError("URL should be last")
				self.url = args[i]
			i += 1
		self.check(opt)

	def check(self, opt):
		''' Check for option validity '''
		if 'l' in opt and 'r' not in opt:
			raise ValueError("Depth option without recursive")
		if 'l' in opt and (self.depth < 0 or self.depth > 1000):
			raise ValueError("Invalid depth (must be between 0 and 1000)")
		
		''' Check for folder path '''
		os.makedirs(self.path, exist_ok=True)
		if self.path[-1] != '/':
			self.path += "/"

	def scrap(self, url, depth=None):
		elements = []
		links = []

		if url in self.done:
			return
		
		''' Get the page content '''
		res = requests.get(url)
		if not res.ok:
			return
		
		soup = BeautifulSoup(res.text, 'html.parser')

		''' Parse and store each image url '''
		elements = soup.find_all("img")
		links = [img.get("src") for img in elements]

		''' Download each images '''
		for x in links:
			filename = utils.get_img_name(x)
			if not filename or x == None:
				continue
			filepath = self.path + filename
			img_url = urllib.parse.urljoin(self.url, x)
			with open(filepath, 'wb') as file:
				file.write(requests.get(img_url).content)

		self.done.append(url)
		elements.clear()
		links.clear()
		''' Scrap all the links in the page'''
		if depth > 0:
			elements = soup.find_all("a")
			links = [img.get("href") for img in elements]
			for x in links:
				if x != None and not x.startswith("#") and not x.startswith("mailto:"):
					link_url = urllib.parse.urljoin(self.url, x)
					self.scrap(link_url, depth - 1)
