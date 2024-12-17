import math

def number_return_module(self, number):
    if self.variables.result == None:
        if len(self.variables.number_list) < 10:
            self.variables.number_list.append(number)
    
    if self.variables.result != None:
        self.variables.result = None
        self.variables.number_list.clear()
        if len(self.variables.number_list) < 10:
            self.variables.number_list.append(number)
            
    self.convert_numbers()
    self.label_down_.configure(text=self.variables.number)
    
def operation_return_module(self, operation):
    self.variables.operator = operation
    if self.variables.number == math.e or self.variables.number == math.pi:
        self.variables.result = None
        self.variables.show_number = self.variables.number
        
    elif self.variables.result is not None:
        self.variables.show_number = self.variables.result
        self.variables.number = self.variables.result
    else:
        self.variables.show_number = self.variables.number
        
    self.variables.number_list.clear()
    self.label_up_.configure(text=f'{self.variables.show_number} {self.variables.operator}')
    self.label_down_.configure(text=f'{self.variables.number} ')
    
def operation_return_module_special(self, operation):
    self.variables.operator = operation
    
    if self.variables.result is not None:
        self.variables.show_number = self.variables.result
        
    else:
        self.variables.show_number = self.variables.number
    
    if self.variables.operator == '1/X':
        if self.variables.show_number == 0:
            self.label_up_.configure(text='Invalid input')
        else:
            self.variables.result = 1 / self.variables.show_number
            self.label_up_.configure(text=f'1/({self.variables.show_number}) = ')
        
    elif self.variables.operator == 'X\u00B2':
        self.variables.result = math.pow(self.variables.show_number, 2)
        self.label_up_.configure(text=f'({self.variables.show_number})\u00B2 = ')
        
    elif self.variables.operator == '\u221AX':
        if self.variables.show_number < 0:
            self.variables.result = 'Invalid input'
        else:
            self.variables.result = math.sqrt(self.variables.show_number)
            self.label_up_.configure(text=f'\u221A({self.variables.show_number}) = ')
    
    self.variables.number_list.clear()
    self.variables.operator = None
    self.variables.number = self.variables.result 
    self.label_down_.configure(text=f'{self.variables.result} ')
    
def delete_module(self):
    if len(self.variables.number_list) > 0: 
        self.variables.number_list.pop()
        self.convert_numbers()
        self.label_down_.configure(text=self.variables.number)
    if len(self.variables.number_list) == 0:
        self.variables.number = 0
        self.label_down_.configure(text=self.variables.number)
    self.variables.operator = ''
        
def convert_numbers_module(self):
    #Converting numbers to int or float
    if not self.variables.number_list:
        self.variables.number = 0
        return
    self.variables.number_string = ''.join(map(str, self.variables.number_list))
    
    if '.' in self.variables.number_string:
        if self.variables.number_string[0] == '.' and len(self.variables.number_string) == 1:
            return
        self.variables.number = float(self.variables.number_string)
    else:
        self.variables.number = int(self.variables.number_string)
    
        
def equal_module(self):
    #
    if self.variables.operator in ['+', '-', 'x', '/',]:
        combine = f'{self.variables.show_number} {self.variables.operator} {self.variables.number} = '
    else:
        combine = self.variables.result
    if self.variables.operator == '+':
        self.variables.result = self.variables.number + self.variables.show_number
    elif self.variables.operator == 'x':
        self.variables.result = self.variables.number * self.variables.show_number
    elif self.variables.operator == '/':
        if self.variables.number == 0:
            self.label_down_.configure(text='Invalid input')
        else:
            self.variables.result = self.variables.show_number / self.variables.number 
    elif self.variables.operator == '-':
        self.variables.result = self.variables.show_number - self.variables.number
    
    if self.variables.operator == 'mod' :
        combine = f'({self.variables.show_number}) {self.variables.operator} ({self.variables.number}) = '
        self.variables.result = self.variables.show_number % self.variables.number
    
    if self.variables.operator == 'x^y':
        combine = f'({self.variables.show_number})^({self.variables.number}) = '
        self.variables.result = math.pow(self.variables.show_number, self.variables.number)
        
    if self.variables.operator == 'log\u2093\u02B8':
        combine = f'log({self.variables.show_number})({self.variables.number}) = '
        self.variables.result = math.log(self.variables.number, self.variables.show_number)
        
    self.label_up_.configure(text=combine)
    self.label_down_.configure(text=self.variables.result)
    self.variables.number_list.clear()
    self.variables.operator = None
    self.variables.number = self.variables.result 
    self.variables.show_number = None

