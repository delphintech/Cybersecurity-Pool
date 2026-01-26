class Vaccine:
    usage = "Usage: ./vaccine [-oX] URL\n \
    options:\n\
        - -o <file_name>: Archive file, if not specified it will be stored in a default one\n \
        - -X <GET|POST>: Type of request, if not specified GET will be used.\n"

    def __init__(self, args):
        self.archive = ""
        self.request = "GET"

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
                        self.request = args[i]
                    case _:
                        raise ValueError("Wrong option")
            else:
                if i < len(args) - 1:
                    raise ValueError("URL should be last")
                self.url = args[i]
            i += 1
            self.check_init()

    def check_init(self):
        # TODO:
        # check if URL is valid and accessible
        # check if the argument of request is valid
        # check if archive file is valid or accessible, create it ?