import os
import sys
import urllib
from form import Form
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

class Vaccine:
    usage = "Usage: ./vaccine [-oX] URL\n \
    options:\n\
        * -o <file_name>: Archive file, if not specified it will be stored in a default one\n \
        * -X <GET|POST>: Type of request, if not specified GET will be used.\n\
        * -d <max_depth>` Maximun crawl depth. 1 by default, maximum 5\n"

    def __init__(self, args):
        self.report = ""
        self.archive = "Report.txt"
        self.request = "GET"
        self.max_depth = 1
        self.url_done = []
        self.forms = []

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
                        self.request = args[i].upper()
                    case 'd':
                        i += 1
                        self.request = args[i]
                    case _:
                        raise ValueError("Wrong option")
            else:
                if i < len(args) - 1:
                    raise ValueError("URL should be last")
                self.url = args[i]
            i += 1
        self.check_args()
        self.init_session()

    def check_args(self):
        # Check if valid request
        if not (self.request == "GET" or self.request == "POST"):
            raise ValueError("Request must be GET or POST")
        # check max depth validity
        if self.max_depth < 0 or self.max_depth > 5:
            raise ValueError("Crawling depth must be between 0 and 5")
        # Check for valid url
        parsed = urlparse(self.url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError("Invalid url")
        # check archive file is valid
        if len(self.archive) > 100:
            raise ValueError("File name must be less than 100 character")
        if os.access(self.archive, os.F_OK) and not os.access(self.archive, os.W_OK):
            raise ValueError("File already exists and lack permission's access")
    
    def init_session(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        self.report('-' * 20 + " VULNERABILITY REPORT " + '-' * 20 + "\n\n")
        self.report("="*70 + "\n")
        self.report(f"Target URL: {self.url}\n")
        self.report(f"Request Method: {self.request}\n")
        self.report(f"Crawl Depth: {self.max_depth}\n")
        self.report("="*70 + "\n\n")
    
    def report(self, text):
        report += text + "\n"
    
    def send(self, url, data):
        if self.request == 'GET':
            return self.session.get(url, params=data)
        elif self.request == 'POST':
            return self.session.post(url, data=data)

    def get_forms(self, url, depth):
        ''' Get all the forms from the url and crawl to set depth '''

        if url in self.url_done:
            return

        print(f"********** {url} | {depth} **********") # DEV

        # Get the page content
        response = self.session.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse and store each form
        for f in soup.find_all('form'):
            form = Form(f)
            if form.method == self.request and form not in self.forms:
              self.forms.append(form)

        self.url_done.append(url)

        # Scrap all the links in the page
        if depth > 0:
          for link in soup.find_all('a', href=True):
            href = link['href']
            if not href.startswith(("#", "mailto:", "javascript")):
                link_url = urllib.parse.urljoin(url, href)
                self.get_forms(link_url, depth - 1)

    def check_all_inputs(self, form, query):
        ''' Check the query with all inputs of the form'''
        responses = []
        data = {}

        i = 0
        while i < len(form):
            for idx, input in self.inputs:
                if idx == i:
                    target = input['name']
                    data[input['name']] = query
                else:
                    data[input['name']] = input['value'] or 'test'
            res = self.send(form.action, data)
            responses.append({
                'input': target,
                'response': res
            })
            i += 1
    
    def check_vulnerability(self):
        if not self.forms:
            print(f"No forms found with {self.request}")
            return

        # Check for Error-based
        


    def __str__(self):
        return (f"Vaccine:\n  * URL:      {self.url}\n\
  * Request:  {self.request}\n * Archive:  {self.archive}")
    
    def clean(self):
        ''' Write report in file and close the session'''
        self.report('-' * 28 + " END " + '-' * 28 + "\n\n")
        with open(self.archive, 'w') as file:
            file.write(self.report)
        session = getattr(self, "session", None)
        if session:
            session.close()

    def __exit__(self):
        self.clean()

    def __del__(self):
        self.clean()
