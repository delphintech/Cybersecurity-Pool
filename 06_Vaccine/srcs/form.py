from selenium import webdriver
from selenium.webdriver.common.by import By

class Form:
    def __init__(self, elements):
        self.action = elements.get_attribute('action')
        self.method = elements.get_attribute('method').upper()
        self.inputs = []

        for input in elements.find_elements(By.TAG_NAME, 'input'):
            if input.get_attribute('type') == "text":
                input_name = input.get_attribute('name') 
                input_value = input.get_attribute('value') 
                self.inputs.append({'name': input_name, 'value': input_value})

    def __eq__(self, other):
        if not isinstance(other, Form):
            return False
        return (self.action == other.action and 
                self.method == other.method and 
                self.inputs == other.inputs)

    def __str__(self):
        inputs = ""
        for input in self.inputs:
            inputs = inputs + f"  Name: {input['name']} | value: {input['value']}\n"
        return (f"Action:  {self.action}\nMethod:  {self.method}\n\
Inputs:\n {inputs}")