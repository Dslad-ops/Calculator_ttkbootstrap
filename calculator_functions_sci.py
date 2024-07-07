import math
#['e', '\u03C0', 'log\u2081\u2080', '10\u02E3', 'x\u02B3' ] #e, pi, log10x, 10powx, xpowy
def operation_return_sci_1_module(self, operation, ):
    self.operation = operation
    
    if self.operation == 'e':
        self.number  = math.e
    
    elif self.operation == '\u03C0':
        self.number  = math.pi
        
    elif self.operation == 'log\u2081\u2080':
        self.number = math.log10(self.show_number)
        
    elif self.operation == '10\u02E3':
        self.number = math.pow(10, self.show_number)
    
    elif self.operation == 'x\u02B3':
        self.result = math.pow(self.show_number, self.number)

    self.label_up_.configure(text=self.number)
    
#['e\u02E3', 'ln', 'log\u2093\u02B8', 'n!', 'mod' ] #epowx, ln, logxy, n!, mod    
def operation_return_sci_2_module(self, operation, ):
    self.operation = operation
    
    if self.operation == 'e\u02E3':
        self.number  = math.exp(self.show_number)
    
    elif self.operation == 'ln':
        self.number  = math.log( self.show_number)
        
    elif self.operation == 'log\u2081\u2080':
        self.result = math.log(self.number, self.show_number)
        
    elif self.operation == 'n!':
        self.number = math.factorial(self.show_number)
    
    elif self.operation == 'mod':
        self.result = self.show_number % self.number

    self.label_up_.configure(text=self.number)

def special_module(self, operation):
    self.operation = operation
    if self.operation == '+/-':
        if self.result:
            self.result = -self.result
            self.label_down_.configure(text=self.result)
        else:
            self.number = -self.number
            self.label_down_.configure(text=self.number)
    elif self.operation == 'Trig':
        pass

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