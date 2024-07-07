import ttkbootstrap as tb
from  tkinter import *
from calculator_functions_sci import *
import math


class ButtonsSci():
    def __init__(self) -> None:
        self.number_list =[]
        self.operation_list = []
        self.number_calclulate = []
        self.operator = None
        self.result = None
        self.number = 0
        self.memory_store = None
        self.show_number = None
        self.buttons_sci_1()
        self.buttons_sci_2()
        self.special_buttons()
        
        
    def operation_return_sci_1(self, number):
        operation_return_sci_1_module(self, number)
        
    def operation_return_sci_2(self, number):
        operation_return_sci_2_module(self, number)
    
    def special(self, operation):
        special_module(self, operation)
         
    def buttons_sci_1(self):       
        operator_list = ['e', '\u03C0', 'log\u2081\u2080', '10\u02E3', 'x\u02B3' ] #e, pi, log10x, 10powx, xpowy
        for i in range(5):
            self.button_sci_1 = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.operation_return_sci_1(x))
            self.button_sci_1.grid(column = i, row = 2, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)  
    
    def buttons_sci_2(self):       
        operator_list = ['e\u02E3', 'ln', 'log\u2093\u02B8', 'n!', 'mod' ] #epowx, ln, logxy, n!, mod 
        for i in range(5):
            self.button_sci_2 = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.operation_return_sci_2(x))
            self.button_sci_2.grid(column = i, row = 3, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)     
    
        
    def special_buttons(self):
        operator_list = ['M+', 'M-', 'MR',]
        for i in range(3):
            self.button_memory = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.memory(x))
            self.button_memory.grid(column = i, row = 2, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1) 
        
            self.button_special = tb.Button(style = 'success', 
                                            padding = 10, 
                                            text = '+/-', 
                                            command = self.special('+/-'))
            self.button_special.grid(column = 3 , row = 2, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        
        self.trig = tb.Menubutton(bootstyle = 'danger', text = 'Trig')
        self.trig.grid(column = 4, row = 2, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        self.menu_data = tb.Menu(self.trig)
        item_var = StringVar()
        for x in ['sin', 'cos', 'tan', 'cotan']:
            self.menu_data.add_radiobutton(label = x, variable = item_var, command = lambda x: self.trig_menu(x))
        self.trig['menu'] = self.menu_data