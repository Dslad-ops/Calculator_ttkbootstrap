import ttkbootstrap as tb
from  tkinter import *
from calculator_functions_main import *
from calculator_functions_sci import *


class Buttons():
    def __init__(self, master = None, label_down=None, label_up=None, variables = None) -> None:
        self.master = master
        self.variables = variables
        self.label_down_ = label_down
        self.label_up_ = label_up
        
        
    def number_return(self, number):
        number_return_module(self, number)   
        
    def operation_return(self, operation):
        operation_return_module(self, operation)
    
    def operation_return_special(self, operation):
        operation_return_module_special(self, operation)
    
    def delete(self):
        delete_module(self)
    
    def convert_numbers(self):
        convert_numbers_module(self)
        
    def equal(self, ):
        equal_module(self)
    
    def special(self, operation):
        special_module(self, operation)
        
    def trig_menu(self, operation):
        trig_menu_module(self, operation)

        
    def number_buttons(self, master):
        #Creating buttons
        self.x = 1
        for i in range(3):
            for j in range(3):
                self.button = tb.Button(style = 'primary', 
                                        padding = 10, 
                                        text = f'{self.x}', 
                                        command = lambda x=self.x:self.number_return(x))
                self.button.grid(column = j, row = i+5, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
                self.x += 1

        self.button_0 = tb.Button(style = 'primary', padding = 10, text = 0, command = lambda:self.number_return(0))
        self.button_0.grid(column = 1, row = 8, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        
        self.delete_button = tb.Button(style = 'danger', padding = 10, text = '<<', command = self.delete)
        self.delete_button.grid(column = 0, row = 8, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        
        self.button_dot = tb.Button(bootstyle = 'primary', padding = 10, text = '.', command = lambda: self.number_return('.'))
        self.button_dot.grid(column = 2, row = 8, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)  
  
    def operation_buttons(self, master):
        #Creating buttons
        operator_list = [ '+', '-', 'x', '/', ]
        for i in range(4):
            self.button_operator = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.operation_return(x))
            self.button_operator.grid(column = 4, row = i+5, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)  
             
        operator_list = ['1/X', 'X\u00B2', '\u221AX'] 
        for i in range(3):
            self.button_operator = tb.Button(style = 'info', 
                                             padding = 10, 
                                             text = f'{operator_list[i]}', 
                                             command = lambda x=operator_list[i]:self.operation_return_special(x))
            self.button_operator.grid(column = 3, row = i+5, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)  
            
        self.button_equal = tb.Button(bootstyle = 'success' , 
                                             padding = 10, 
                                             text = '=' , 
                                             command = self.equal)
        self.button_equal.grid(column = 3, row = 8, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1 )
        

        
        self.trig = tb.Menubutton(bootstyle = 'danger', text = 'Trig')
        self.trig.grid(column = 4, row = 4, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        self.menu_data = tb.Menu(self.trig)
        item_var = StringVar()
        operator_list = ['sin', 'cos', 'tan', 'cotan']
        for i in range(4):
            self.menu_data.add_radiobutton(label = f'{operator_list[i]}', variable = item_var, command = lambda x=operator_list[i]: self.trig_menu(x))
        self.trig['menu'] = self.menu_data