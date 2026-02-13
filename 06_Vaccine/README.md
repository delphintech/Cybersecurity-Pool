# VACCINE
**Vaccine** is a SQL injection program compatible with
TODO
It runs the following tests:
 TODO
To provide, if possible, the following informations:
- The vulnerable parameters.
- The payload used.
- Database names.
- Table names.
- Column names.
- Complete database dump.

## Setup

`make` Create environment and executable

`make clean` Stop environment and delete exec

## Usage
  ./vaccine [-oXd] URL

  - `-o <file_name>` Archive file, if not specified it will be stored in a default one
  - `-X <GET|POST>` Type of request, if not specified GET will be used.
  - `-d <max_depth>` Maximun crawl depth. 0 by default, 5 as a maximum

## Test

**Check the norm**\
`make norm` 

**Websites to test the program**
`http://testphp.vulnweb.com/` MySQL db and POST Request
`http://testphp.vulnweb.com/artists.php?artist=1` MySQL and GET Request

`http://testasp.vulnweb.com/` 

`https://www.hackthissite.org/` Too slow

`http://www.itsecgames.com`

`https://demo.owasp-juice.shop/#/`  No form founr


`https://google-gruyere.appspot.com/part1` Microsoft db with POST


# "https://demo.testfire.net/login.jsp"


Error: The used SELECT statements have a different number of columns