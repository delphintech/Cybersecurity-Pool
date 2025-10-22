from cryptography.fernet import Fernet
import time

USAGE = "usage: ./ft_opt [options]\n \
	options:\n\
		-g [64_HEXA_KEY], store the key inciprted in ft_otp.key\n\
		-k [FILE / KEY], generates a new temporary password based on the key given"

KEY="b'IgkaT-cTRq5rV386nDbf_hXkz7WSCvWb6nc19Tt7_2A='"

def is_valid_hexa_key(arg):
	dic = "0123456789abcdefABCDEF"

	if len(arg < 64) or len(arg) > 72:
		return False
	for c in arg:
		if c not in dic:
			return False
	return True

def	store_key(key):
	fernet = Fernet(KEY)
	encrypt = fernet.encrypt(key)
	with open("ft_otp.key", "w") as file:
		file.write(encrypt)
	print("Key was successfully saved in ft_otp.key.\n")

def	decrypt_key(file):
	fernet = Fernet(KEY)
	with open(file, "r") as file:
		encrypt = file.read()
	decrypt = fernet.decrypt(encrypt)
	if not is_valid_hexa_key(decrypt):
		print("The given key is invalid\n")
		return
	return decrypt

def generate_pwd(key):
	# TODO: HOTP algorithm
	curr = time.time()
	return
