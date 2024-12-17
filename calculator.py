import ttkbootstrap as tb
from button_label_main import Buttons
from button_label_sci import ButtonsSci
from shared_variables_class import CalculatorVariables


    
class CalculatorApp(tb.Window):
    def __init__(self, themename = 'cerculean',  ):
        super().__init__(themename = themename)
        self.title("Calculator")
        self.geometry('1000x1000')
        self.columnconfigure((0,1,2,3,4,), weight = 1, pad= 5, uniform = True)
        self.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1, pad = 5, uniform = True)
        variables = CalculatorVariables()
        self.label_frame_for_numbers()
        self.labels_for_numbers()
        
        buttons_sci = ButtonsSci(master = self, 
                                 label_down=self.label_down_, 
                                 label_up=self.label_up_, 
                                 variables = variables)
        
        buttons = Buttons(master = self, 
                          label_down=self.label_down_, 
                          label_up=self.label_up_, 
                          variables = variables)
    
        buttons.number_buttons(self)
        buttons.operation_buttons(self)
        buttons_sci.buttons_sci_1(self)
        buttons_sci.buttons_sci_2(self)
        buttons_sci.special_buttons(self)
        
        
    def labels_for_numbers(self):
        self.label_down_ = tb.Label(self.label_frame,
                                  text = 0,
                                  font = ('sans-serif', 12),
                                  )
        self.label_down_.grid(column = 0, row = 1, columnspan = 5, sticky = 'nsew', padx = 10, pady = 10)
        
        self.label_up_= tb.Label(self.label_frame,
                                  text = '', 
                                  font = ('sans-serif', 12),
                                  )
        self.label_up_.grid(column = 0, row = 0, columnspan = 5, sticky = 'nsew', padx = 10, pady = 10)
    
    def label_frame_for_numbers(self, ):
         self.label_frame = tb.Labelframe( style = 'warning') 
         self.label_frame.grid(column = 0, row = 0, columnspan = 5, rowspan = 2, sticky = 'nsew', padx = 5, pady = 5) 
    
 
if __name__ == '__main__':
    app = CalculatorApp()
    app.mainloop()

