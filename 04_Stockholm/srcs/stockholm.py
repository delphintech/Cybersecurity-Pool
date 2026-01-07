class Stockholm:
	def __init__(self, args):
		self.options = ""
		self.key = ""

		i = 0
		while i < len(args):
			if args[i] == "-r" or args[i] == "-reverse":
				self.options.__add__("r")
			elif args[i] == "-h" or args[i] == "-help":
				self.options.__add__("h")
			elif args[i] == "-v" or args[i] == "-version":
				self.options.__add__("v")
			elif args[i] == "-s" or args[i] == "-silent":
				self.options.__add__("s")
			else:
				if i < len(args) - 1:
					raise ValueError("Invalid option: {args[i]}")
				if len(args[i]) < 16
					raise ValueError("Encryptiion key must be at least 16 characters long")
				self.key = args[i]
