#!/usr/bin/env python3
import sys
from vaccine import Vaccine

def main():
    args = sys.argv[1:]
    if not args:
        print(Vaccine.usage)
        sys.exit(1)

    try:
        vaccine = Vaccine(args)
        # TODO: Get all website froms corresponding of the chosen method
        # TODO: Check for sql error message in the response
        # TODO: Test different SQL injection with special characters 
        #       to see if response contains SQl error indicating vulnerability
    except ValueError as e:
        print(e + "\n\n" + Vaccine.usage)

    except Exception as e:
        print(e)


# Laumch main only if called directly
if __name__ == "__main__":
    main()
