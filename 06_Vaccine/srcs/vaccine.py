import os
import urllib
from form import Form
from urllib.parse import urlparse
import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup

class Vaccine:
    usage = "Usage: ./vaccine [-oX] URL\n \
    options:\n\
        * -o <file_name>: Archive file, if not specified it will be stored in a default one\n \
        * -X <GET|POST>: Type of request, if not specified GET will be used.\n\
        * -d <max_depth>` Maximun crawl depth. 1 by default, maximum 5\n"

    queries_check = {
        'error': ["'"],
        'boolean': ["' AND 1=1 --", "' AND 1=2 --"],
        'union': ["' UNION SELECT NULL--", "' UNION SELECT NULL, NULL--", "' UNION SELECT NULL, NULL, NULL--"],
        'sleep': ["1' AND SLEEP(5)--"]
    }

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
        self.add_report(('-' * 20 + " VULNERABILITY REPORT " + '-' * 20).center(70) + "\n\n")
        self.add_report("+" + "-" * 68 + "")
        self.add_report("|".ljust(69) + "|")
        self.add_report(f"|  Target URL: {self.url}".ljust(69) + "|")
        self.add_report("|".ljust(69) + "|")
        self.add_report(f"|  Request Method: {self.request}".ljust(69) + "|")
        self.add_report("|".ljust(69) + "|")
        self.add_report(f"|  Crawl Depth: {self.max_depth}".ljust(69) +"|")
        self.add_report("|".ljust(69) + "|")
        self.add_report("+" + "-" * 68 + "\n\n")
    
    def add_report(self, text):
        self.report += text + "\n"
    
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

    # def check_form(self, form, query):
    #     ''' Check the form with the given query '''
    #     data = {}

    #     for input in self.inputs:
    #         data[input['name']] = query
    #     return self.send(form.action, data)
    
    def check_vulnerability(self):
        ''' Check different vulnerabilities '''
        if not self.forms:
            self.add_report(f"NO FORMS FOUND WITH{self.request}")
            return

        # Error-based

        query = self.queries_check['error'][0]
        for form in self.forms:
            responses = self.check_all_inputs(form, query)
            for res in responses:
                if res.status_code == 500:
                    form.vul = True
                    list(filter({form.inputs['name'] == res['input']}, form.inputs))[0]['vul'].append("error")
        
        # Boolean
        true_query = self.queries_check['boolean'][0]
        false_query = self.queries_check['boolean'][1]
        for form in self.forms:
            true_responses = self.check_all_inputs(form, true_query)
            false_responses = self.check_all_inputs(form, false_query)
            for true_res, false_res in zip(true_responses, false_responses):
                if len(true_res.text) != len(false_res.text):
                    form.vul = True
                    list(filter({form.inputs['name'] == res['input']}, form.inputs))[0]['vul'].append("boolean")


        # Union
        one_query = self.queries_check['error'][0]
        two_query = self.queries_check['union'][1]
        three_query = self.queries_check['union'][3]
        for form in self.forms:
            one_responses = self.check_all_inputs(form, one_query)
            two_responses = self.check_all_inputs(form, two_query)
            three_responses = self.check_all_inputs(form, three_query)
            for one, two, three in zip(one_responses, two_responses, three_responses):
                if len(one.text) != len(two.text) or len(one.text) != len(three.text):
                    form.vul = True
                    list(filter({form.inputs['name'] == res['input']}, form.inputs))[0]['vul'].append("union")

        self.report_vulnerability()
        # Time-based
        # TODO
        # query =  "1' AND SLEEP(5)--"

    
    def report_vulnerability(self):
        self.add_report("=" * 70)
        self.add_report("VULNERABILITY CHECK".center(70))
        self.add_report("=" * 70 + "\n")

        # Error based:
        for check in self.queries_check:
            self.add_report(f"=== Check: {check.key}, with: \n")
            self.add_report(f"       -> {" \n       -> ".join(check.value)}\"")
            self.add_report(f"\n\n")
        
        for form in self.forms:
            self.add_report(f"== Form tested: {form.action}\n")
            table = PrettyTable()
            list_check = ( check.key for check in self.queries_check )
            table.field_names =  list_check.insert(0, "Input")
            for input in form.inputs:
                row = [input['name']]
                for check in list_check:
                    vul = "V" if check in input['vul'] else " "
                    row.append(vul)
                table.add_row(row)
            self.add_report(table)
            self.add_report("\n\n")

    def __str__(self):
        return (f"Vaccine:\n  * URL:      {self.url}\n\
  * Request:  {self.request}\n * Archive:  {self.archive}")
    
    def clean(self):
        ''' Write report in file and close the session'''
        self.add_report(('-' * 28 + " END " + '-' * 28).center(70))
        with open(self.archive, 'w') as file:
            file.write(self.report)
        session = getattr(self, "session", None)
        if session:
            session.close()

    def __exit__(self):
        self.clean()

    def __del__(self):
        self.clean()
