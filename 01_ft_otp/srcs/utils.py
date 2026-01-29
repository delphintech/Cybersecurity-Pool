from cryptography.fernet import Fernet
import time
import hmac
import os

USAGE = "usage: ./ft_opt [options]\n \
	options:\n\
		-g [64_HEXA_KEY], store the encrypted key in ft_otp.key\n\
		-k [FILE / KEY], generates a new temporary password based on the key given"

KEY=b"IgkaT-cTRq5rV386nDbf_hXkz7WSCvWb6nc19Tt7_2A="

def valid_hexa_key(arg):
	dic = "0123456789abcdefABCDEF"
	key = arg

	if os.access(arg, os.R_OK):
		with open(arg, "r") as file:
			key = file.read()
	key = key.rstrip(" \n")
	if len(key) < 64 or len(key) > 72:
		return ""
	for c in key:
		if c not in dic:
			return ""
	return key

def	store_key(key):
	fernet = Fernet(KEY)
	bkey = key.encode()
	encrypt = fernet.encrypt(bkey)
	with open("ft_otp.key", "wb") as file:
		file.write(encrypt)
	print("Key was successfully saved in ft_otp.key.\n")

def	decrypt_key(file):
	fernet = Fernet(KEY)
	with open(file, "rb") as file:
		encrypt = file.read()
	decrypt = fernet.decrypt(encrypt)
	key = decrypt.decode()
	if not valid_hexa_key(key):
		print("The given key is invalid\n")
		return
	return key

def generate_hs(key, counter):
	bcounter = counter.to_bytes(8, byteorder="big")	# converte int to byte (take big endian as per RFC 4226)
	bkey = bytes.fromhex(key)
	hs_hmac = hmac.new(bkey, bcounter, "sha1")	# generate HMAC-SHA-1 value (160 bytes)
	return hs_hmac.digest()	# Compute HMAC-SHA-1 to 20 bytes

# Truncation function given in RFC 4226
def	dynamic_truncation(hs):
    # DT(String) // String = String[0]...String[19]
	offset = hs[19] & 0b1111 #  Let OffsetBits be the low-order 4 bits of String[19]
	#  Offset = StToNum(OffsetBits) // 0 <= OffSet <= 15: (already a number)
	#	Let P = String[OffSet]...String[OffSet+3]
	p = hs[offset:offset + 4]
    #  Return the Last 31 bits of P (P has 4 bytes so 32 bits)
	res = bytearray()
	res.append(p[0] & 0x7f) # takes the first seventh
	for b in p[1:]:
		res.append(b & 0xff) # takes all of the rest
	return res

# Computation given in RC 4226
def	compute_hotp(trunc):
#    Let Snum  = StToNum(Sbits)   // Convert S to a number in 0...2^{31}-1 (so a int)
	num = int.from_bytes(trunc, "big")
#    Return D = Snum mod 10^Digit //  D is a number in the range 0...10^{Digit}-1 (we want 6 number so 10^6 - 1)
	return num % 10 ** 6

def generate_pwd(key):
	# Step 1: Generate an HMAC-SHA-1 value Let HS = HMAC-SHA-1(K,C)  // HS is a 20-byte string
	counter = int(time.time()) // 30 # takes current time as counter and change every 30 seconds
	hs = generate_hs(key, counter)
	# Step 2: Generate a 4-byte string (Dynamic Truncation)
	trunc = dynamic_truncation(hs)
	# Step 3: Compute an HOTP value
	otp = compute_hotp(trunc)
	return f"{otp:06d}"	# string of 6 digits including the 0
