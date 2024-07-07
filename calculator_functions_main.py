import math

def number_return_module(self, number):
    self.result = None
    if len(self.number_list) < 10:
        self.number_list.append(number)
    self.convert_numbers()
    self.label_down_.configure(text=self.number)
    
def operation_return_module(self, operation):
    self.operator = operation
    if self.result is not None:
        self.show_number = self.result
        self.number = self.result
    else:
        self.show_number = self.number
    self.number_list.clear()
    self.label_up_.configure(text=f'{self.show_number} {self.operator}')
    self.label_down_.configure(text=f'{self.number} ')
    
def operation_return_module_special(self, operation):
    self.operator = operation
    if self.result is not None:
        self.show_number = self.result
        # self.result  = None
    else:
        self.show_number = self.number
    
    if self.operator == '1/X':
        if self.show_number == 0:
            self.label_up_.configure(text='Invalid input')
        else:
            self.result = 1 / self.show_number
            self.label_up_.configure(text=f'1/({self.show_number}) = ')
        
    elif self.operator == 'X\u00B2':
        self.result = math.pow(self.show_number, 2)
        self.label_up_.configure(text=f'({self.show_number})\u00B2 = ')
        
    elif self.operator == '\u221AX':
        if self.show_number < 0:
            self.result = 'Invalid input'
        else:
            self.result = math.sqrt(self.show_number)
            self.label_up_.configure(text=f'\u221A({self.show_number}) = ')
    
    self.number_list.clear()
    self.operator = None
    self.number = self.result 
    self.label_down_.configure(text=f'{self.result} ')
    
def delete_module(self):
    if len(self.number_list) > 0: 
        self.number_list.pop()
        self.convert_numbers()
        self.label_down_.configure(text=self.number)
    if len(self.number_list) == 0:
        self.number = 0
        self.label_down_.configure(text=self.number)
    self.operator = ''
        
def convert_numbers_module(self):
    if not self.number_list:
        self.number = 0
        return
    self.number_string = ''.join(map(str, self.number_list))
    
    if '.' in self.number_string:
        if self.number_string[0] == '.' and len(self.number_string) == 1:
            return
        self.number = float(self.number_string)
    else:
        self.number = int(self.number_string)
    
        
def equal_module(self):
    
    if self.operator in ['+', '-', 'x', '/',]:
        combine = f'{self.show_number} {self.operator} {self.number} = '
    else:
        combine = self.result
    if self.operator == '+':
        self.result = self.number + self.show_number
    elif self.operator == 'x':
        self.result = self.number * self.show_number
    elif self.operator == '/':
        if self.number == 0:
            self.label_down_.configure(text='Invalid input')
        else:
            self.result = self.show_number / self.number 
    elif self.operator == '-':
        self.result = self.show_number - self.number
    
    self.label_up_.configure(text=combine)
    self.label_down_.configure(text=self.result)
    self.number_list.clear()
    self.operator = None
    self.number = self.result 
    
def memory_module(self, operation):
    self.operation = operation
    if self.operation == 'M+':
        self.memory_store = self.number
            
    elif self.operation == 'M-':
        self.memory_store = None
        
    elif self.operation == 'MR':
        self.number = self.memory_store
        self.label_down_.configure(text=self.number)
        self.result = None
        

def trig_menu_module(self,input):
    if input =='sin':
        self.result = math.sin(self.number)
    elif input == 'cos':
        self.result = math.cos(self.number)
    elif input == 'tan':
        self.result = math.tan(self.number)
    elif input == 'cotan':
        self.result = math.atan(self.number)
    self.label_down_.configure(text=self.result)