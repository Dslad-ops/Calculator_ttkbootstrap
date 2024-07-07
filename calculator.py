import ttkbootstrap as tb
from button_label_main import Buttons
from button_label_sci import ButtonsSci
import math

        
        

window = tb.Window(themename = 'cerculean', title = 'Calculator', )
window.geometry('1000x1000')
window.columnconfigure((0,1,2,3,4,), weight=1, pad=5, uniform=True)
window.rowconfigure((0,1,2,3,4,5,6,7,8), weight =1, pad = 5, uniform = True)


buttons_sci = ButtonsSci()
buttons = Buttons()
buttons.label_frame_for_numbers()
buttons.special_buttons()
buttons.number_buttons()
buttons.operation_buttons()
buttons_sci.buttons_sci_1()
buttons_sci.buttons_sci_2()
window.mainloop()

