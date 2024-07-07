import ttkbootstrap as tb
from  tkinter import *
from calculator_functions_main import *
from button_label_sci import ButtonsSci

class Buttons():
    def __init__(self) -> None:
        self.number_list =[]
        self.operation_list = []
        self.number_calclulate = []
        self.operator = None
        self.result = None
        self.number = 0
        self.memory_store = None
        self.show_number = None
        self.buttons_sci = ButtonsSci()
       
        
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
    
    def memory(self, operation):
        memory_module(self, operation)

        
    def number_buttons(self):
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
    
    def label_frame_for_numbers(self):
        self.label_frame = tb.Labelframe( style = 'warning') 
        self.label_frame.grid(column = 0, row = 0, columnspan = 5, rowspan = 2, sticky = 'nsew', padx = 5, pady = 5)   
        
    def label_down(self):
        self.label_down_ = tb.Label(
                                  text =0,
                                  font = ('sans-serif', 12),
                                  )
        self.label_down_.grid(column = 0, row = 1, columnspan = 5, sticky = 'nsew', padx = 10, pady = 10)
        
    def label_up(self):
        self.label_up_= tb.Label(
                                  text = '', 
                                  font = ('sans-serif', 12),
                                  )
        self.label_up_.grid(column = 0, row = 0, columnspan = 5, sticky = 'nsew', padx = 10, pady = 10)
        
    def operation_buttons(self):
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
        
    def special_buttons(self):
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
                                            command = self.special('+/-'))
            self.button_special.grid(column = 3 , row = 4, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        
        self.trig = tb.Menubutton(bootstyle = 'danger', text = 'Trig')
        self.trig.grid(column = 4, row = 4, sticky = 'nsew', padx = 10, pady = 10, rowspan = 1, columnspan = 1)
        self.menu_data = tb.Menu(self.trig)
        item_var = StringVar()
        for x in ['sin', 'cos', 'tan', 'cotan']:
            self.menu_data.add_radiobutton(label = x, variable = item_var, command = lambda x: self.trig_menu(x))
        self.trig['menu'] = self.menu_data