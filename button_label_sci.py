import ttkbootstrap as tb
from  tkinter import *
from calculator_functions_sci import *



class ButtonsSci():
    def __init__(self, master = None, label_up = None, label_down = None, variables = None) -> None:
        self.master = master
        self.variables = variables
        self.label_down_ = label_down
        self.label_up_ = label_up
        
    def memory(self, operation):
        memory_module(self, operation) 
    
    def operation_return_module_sci(self, operation):
        operation_return_module_sci_module(self, operation)
        
    def operation_return_sci_1(self, number):
        operation_return_sci_1_module(self, number)
        
    def operation_return_sci_2(self, number):
        operation_return_sci_2_module(self, number)
    
    def special(self, ):
        special_module(self, )
         
    def buttons_sci_1(self, master):       
        operator_list = ['e', '\u03C0', 'log\u2081\u2080', '10\u02E3', 'x^y' ] #e, pi, log10x, 10powx, xpowy
        for i in range(5):
            self.button_sci_1 = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.operation_return_sci_1(x))
            self.button_sci_1.grid(column = i, row = 2, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)  
    
    def buttons_sci_2(self, master):       
        operator_list = ['e\u02E3', 'ln', 'log\u2093\u02B8', 'n!', 'mod' ] #epowx, ln, logxy, n!, mod 
        for i in range(5):
            self.button_sci_2 = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.operation_return_sci_2(x))
            self.button_sci_2.grid(column = i, row = 3, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)     
    
        
    def special_buttons(self, master):
        operator_list = ['M+', 'M-', 'MR',]
        for i in range(3):
            self.button_memory = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.memory(x))
            self.button_memory.grid(column = i, row = 4, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1) 
        
        self.button_special = tb.Button(style = 'success', 
                                            padding = 10, 
                                            text = '+/-', 
                                            command = self.special)
        self.button_special.grid(column = 3 , row = 4, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        
        