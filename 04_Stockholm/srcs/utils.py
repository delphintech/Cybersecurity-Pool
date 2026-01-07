USAGE = "usage: ./stockholm [options] KEY\n \
	options:\n\
		- -h, -help : display the help\n \
		- -v, -version: Display program's version\n \
		- -r, -reverse: reverse the infection using the given key\n \
		- -s, -silent: Do not display the encrypted files\n"

def help:
	print(USAGE)
	print("Ransomware that only affects files whose extensions have been affected by **Wannacry**, inside a folder named **infection** inside **HOME** directory.")
	print("\nThe Key given to encrypt must be at least 16 characters long\n")
	print("\nAll the affected files while are renamed  with a .ft extension\n")
