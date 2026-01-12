class Stockholm:
	usage = "Usage: ./stockholm [options] KEY\n \
	options:\n\
		- -h, -help : display the help\n \
		- -v, -version: Display program's version\n \
		- -r, -reverse: reverse the infection using the given key\n \
		- -s, -silent: Do not display the encrypted files\n"

	@classmethod
	def help(cls):
		print(cls.usage)
		print("Ransomware that only affects files whose extensions have been affected by WANNACRY, inside a folder named INFECTION inside HOME directory.\n")
		print(" * The key given to encrypt must be at least 16 characters long\n")
		print(" * All the affected files while are renamed  with a .ft extension\n")

	def version():
		print("v1.0.0")

	def __init__(self, args):
		self.options = ""
		self.key = ""
		self.display = true

		i = 0
		while i < len(args):
			if args[i] == "-r" or args[i] == "-reverse":
				self.options += "r"
			elif args[i] == "-h" or args[i] == "-help":
				self.options += "h"
			elif args[i] == "-v" or args[i] == "-version":
				self.options += "v"
			elif args[i] == "-s" or args[i] == "-silent":
				self.options += "s"
			else:
				if i < len(args) - 1:
					raise ValueError(f"Invalid option: {args[i]}")
				if len(args[i]) < 16:
					raise ValueError("Encryptiion key must be at least 16 characters long")
				self.key = args[i]
			i += 1

	def encrypt(self):
		# TODO

	def reverse(self):
		# TODO

	def print(self):
		print(f"Options: ")
		for o in self.options:
			print(f"  - {o}")
		print(f"Key: {self.key}")