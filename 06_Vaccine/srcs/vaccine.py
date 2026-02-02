import os
import urllib
from form import Form
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Vaccine:
    usage = "Usage: ./vaccine [-oX] URL\n \
    options:\n\
        * -o <file_name>: Archive file, if not specified it will be stored in a default one\n \
        * -X <GET|POST>: Type of request, if not specified GET will be used.\n\
        * -d <max_depth>` Maximun crawl depth. 1 by default, maximum 5\n"

    def __init__(self, args):
        self.archive = ""
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
        ''' create session '''
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
    
    def get_forms(self, url, depth):
        ''' Get all the forms from the url and crawl to set depth '''
        elements = []
        links = []

        if url in self.url_done:
            return

        print(f"********** {url} | {depth} **********") # DEV

        # Get the page content
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        if not self.driver.current_url:
            return

        # Parse and store each form
        elements = self.driver.find_elements(By.TAG_NAME, "form")
        for e in elements:
            form = Form(e)
            if form.method == self.request and form not in self.forms:
              self.forms.append(form)

        self.url_done.append(url)
        elements.clear()

        # Scrap all the links in the page
        if depth > 0:
          elements = self.driver.find_elements(By.TAG_NAME, "a")
          links = [e.get_attribute("href") for e in elements]
          for x in links:
              if x != None and not x.startswith("#") and not x.startswith("mailto:") \
                  and not x.startswith("javascript"):
                  link_url = urllib.parse.urljoin(self.url, x)
                  self.get_forms(link_url, depth - 1)
    
    def __str__(self):
        return (f"Vaccine:\n  * URL:      {self.url}\n\
  * Request:  {self.request}\n * Archive:  {self.archive}")

    def __del__(self):
        driver = getattr(self, "driver", None)
        if driver:
            driver.quit()
