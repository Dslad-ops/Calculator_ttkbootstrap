import math

def operation_return_module_sci_module(self, operation):
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
    self.label_up_.configure(text=f'({self.variables.show_number}) {self.variables.operator}')
    self.label_down_.configure(text=f'{self.variables.number} ')
    
#['e', '\u03C0', 'log\u2081\u2080', '10\u02E3', 'x\u02B3' ] #e, pi, log10x, 10powx, xpowy
def operation_return_sci_1_module(self, operation, ):
    self.variables.operation = operation
        
    if self.variables.operation == 'e':
        self.variables.number = float(math.e)
        self.label_down_.configure(text=self.variables.number)
        self.variables.result = None
        
    elif self.variables.operation == '\u03C0':
        self.variables.number = float(math.pi)
        self.label_down_.configure(text=self.variables.number)
        self.variables.result = None
        
    elif self.variables.operation == 'log\u2081\u2080':
        self.variables.result = math.log10(self.variables.number)
        self.label_up_.configure(text=f'log\u2081\u2080({self.variables.number}) = ')
        self.label_down_.configure(text=self.variables.result)
        self.variables.number = self.variables.result
        
    elif self.variables.operation == '10\u02E3':
        self.variables.result = math.pow(10, self.variables.number)
        self.label_up_.configure(text=f'10^{self.variables.number}')
        self.label_down_.configure(text=self.variables.result)
        self.variables.number = self.variables.result
        
    elif self.variables.operation == 'x^y':
        self.operation_return_module_sci(operation)
        self.label_up_.configure(text=f'({self.variables.show_number})^')
        
    # self.variables.number = self.variables.result
    self.label_down_.configure(text=self.variables.result)    
    
    
#['e\u02E3', 'ln', 'log\u2093\u02B8', 'n!', 'mod' ] #epowx, ln, logxy, n!, mod    
def operation_return_sci_2_module(self, operation, ):
    self.variables.operation = operation
    
    if self.variables.operation == 'e\u02E3':
        self.variables.result  = math.exp(self.variables.number)
        self.label_up_.configure(text=(f'e^({self.variables.number})='))
        
    elif self.variables.operation == 'ln':
        self.variables.result  = math.log( self.variables.number)
        self.label_up_.configure(text=(f'ln({self.variables.number})='))
        
    elif self.variables.operation == 'log\u2093\u02B8':
        self.operation_return_module_sci(operation)
        
    elif self.variables.operation == 'n!':
        if self.variables.number < 0:
            raise ValueError('Cant do a factorial of negative number')
        else:
            self.variables.result = math.gamma(self.variables.number+1)
            self.label_up_.configure(text=(f'({self.variables.number})!'))
        
    elif self.variables.operation == 'mod':
        self.operation_return_module_sci(operation)
        
        
    self.variables.number = self.variables.result
    self.label_down_.configure(text=self.variables.result)

def special_module(self ):
    
    if self.variables.result:
        self.variables.result =- self.variables.result
        self.label_down_.configure(text=self.variables.result)
    else:
        self.variables.number =- self.variables.number
        self.label_down_.configure(text=self.variables.number)
   
def memory_module(self, operation):
    self.variables.operation = operation
    if self.variables.operation == 'M+':
        if self.variables.result:
            self.variables.memory_store = self.variables.result
            
        self.variables.memory_store = self.variables.number
            
    elif self.variables.operation == 'M-':
        self.variables.memory_store = None
        
    elif self.variables.operation == 'MR':
        self.variables.number= self.variables.memory_store
        self.label_down_.configure(text=self.variables.number)
        self.variables.result = None
        
def trig_menu_module(self, operation):
    
    if operation =='sin':
        self.variables.result = math.sin((self.variables.number))
    elif operation == 'cos':
        self.variables.result = math.cos(self.variables.number)
    elif operation == 'tan':
        self.variables.result = math.tan(self.variables.number)
    elif operation == 'cotan':
        self.variables.result = math.atan(self.variables.number)
        
    self.label_down_.configure(text=self.variables.result)