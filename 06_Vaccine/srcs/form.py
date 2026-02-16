import requests
from bs4 import BeautifulSoup
import urllib.parse


class Form:
    def __init__(self, url, element):
        self.action = element.get('action', '')
        self.method = (element.get('method') or 'GET').upper()
        self.inputs = []
        self.vul = False
        self.url = urllib.parse.urljoin(url, self.action)

        for input_elem in element.find_all('input'):
            input_type = input_elem.get('type', 'text')

            if input_type not in ['submit', 'button', 'reset', 'image']:
                input_name = input_elem.get('name', '')
                input_value = input_elem.get('value', '')

                if input_name:
                    self.inputs.append({
                        'name': input_name, 
                        'value': input_value,
                        'type': input_type,
                        'vul': [],
                        'col': 1
                    })
        
        for textarea in element.find_all('textarea'):
            textarea_name = textarea.get('name', '')
            textarea_value = textarea.get_text(strip=True)
            
            if textarea_name:
                self.inputs.append({
                    'name': textarea_name,
                    'value': textarea_value,
                    'type': 'textarea'
                })

    def __eq__(self, other):
        if not isinstance(other, Form):
            return False
        return (self.action == other.action and 
                self.method == other.method and 
                self.inputs == other.inputs)

    def __str__(self):
        inputs = ""
        for input in self.inputs:
            inputs = inputs + f" Name: {input['name']} | value: {input['value']}\n"
        return (f"Action:  {self.action}\nMethod:  {self.method}\n\
Inputs:\n {inputs}")