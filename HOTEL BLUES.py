import os
from subprocess import call
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def click_register():
    call(["python", "register1.py"])
    
def click_main():
    call(["python", "registoradmin.py"]) 

def closewin(root):
	root.destroy()

def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) <= 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "THANK YOU!! WE WILL GIVE YOU THE BEST SERVICE""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input  maximum capacity is 10.""\n")
                break    


class HOTEL_MANAGEMENT:
	def __init__(self):
	        root = Tk()
	        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
	        _fgcolor = '#000000'  # X11 color: 'black'
	        _compcolor = '#ffffff' # X11 color: 'white'
	        _ana1color = '#ffffff' # X11 color: 'white'
	        _ana2color = '#ffffff' # X11 color: 'white'
	        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
	            "roman -underline 0 -overstrike 0"
	        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
	            "-slant roman -underline 0 -overstrike 0"
	        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
	            "roman -underline 0 -overstrike 0"

	        root.geometry("963x749+540+110")
	        root.title("BLUES HOTEL")
	        root.configure(background="#d9d9d9")
	        root.configure(highlightbackground="#d9d9d9")
	        root.configure(highlightcolor="black")  
	        

	        self.Frame1 = Frame(root)
	        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
	        self.Frame1.configure(relief=GROOVE)
	        self.Frame1.configure(borderwidth="2")
	        self.Frame1.configure(relief=GROOVE)
	        self.Frame1.configure(background="#d9d9d9")
	        self.Frame1.configure(highlightbackground="#d9d9d9")
	        self.Frame1.configure(highlightcolor="black")
	        self.Frame1.configure(width=925)     

	        self.Message6 = Message(self.Frame1)
	        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
	        self.Message6.configure(background="#d9d9d9")
	        self.Message6.configure(font=font16)
	        self.Message6.configure(foreground="#000000")
	        self.Message6.configure(highlightbackground="#d9d9d9")
	        self.Message6.configure(highlightcolor="black")
	        self.Message6.configure(text='''WELCOME TO BLUES HOTEL''')
	        self.Message6.configure(width=791)

	        #button registor
	        self.Button2 = Button(self.Frame1)
	        self.Button2.place(relx=0.18, rely=0.17, height=103, width=566)
	        self.Button2.configure(activebackground="#d9d9d9")
	        self.Button2.configure(activeforeground="#000000")
	        self.Button2.configure(background="#d9d9d9")
	        self.Button2.configure(disabledforeground="#bfbfbf")
	        self.Button2.configure(font=font14)
	        self.Button2.configure(foreground="#000000")
	        self.Button2.configure(highlightbackground="#d9d9d9")
	        self.Button2.configure(highlightcolor="black")
	        self.Button2.configure(pady="0")
	        self.Button2.configure(text='''New User Registration''')
	        self.Button2.configure(width=566)
	       	self.Button2.configure(command=click_register)
	       # self.Button2.configure(command=lambda:[click_register,closewin])

	        #button Admin
	        self.Button3 = Button(self.Frame1)
	        self.Button3.place(relx=0.18, rely=0.33, height=93, width=566)
	        self.Button3.configure(activebackground="#d9d9d9")
	        self.Button3.configure(activeforeground="#000000")
	        self.Button3.configure(background="#d9d9d9")
	        self.Button3.configure(disabledforeground="#bfbfbf")
	        self.Button3.configure(font=font14)
	        self.Button3.configure(foreground="#000000")
	        self.Button3.configure(highlightbackground="#d9d9d9")
	        self.Button3.configure(highlightcolor="black")
	        self.Button3.configure(pady="0")
	        self.Button3.configure(text='''Admin Login''')
	        self.Button3.configure(width=566)
	        self.Button3.configure(command=click_main)

			#guest

	        
	        # self.Button3.configure(disabledforeground="#bfbfbf")
	        # self.Button3.configure(foreground="#000000")
	        # self.Button3.configure(highlightbackground="#ffffff")
	        # self.Button3.configure(highlightcolor="black")
	        # self.Button3.configure(pady="0")self.Label4 = Label()
	        # self.Label4.place(relx=0.056, rely=0.60, height=47, width=300)
	        # self.Label4.configure(activebackground="#ffffff")
	        # self.Label4.configure(activeforeground="black")
	        # self.Label4.configure(background="#ffffff")
	        # self.Label4.configure(disabledforeground="#bfbfbf")
	        # #self.Label4.configure(font=font12)
	        # self.Label4.configure(foreground="#000000")
	        # self.Label4.configure(highlightbackground="#ffffff")
	        # self.Label4.configure(highlightcolor="black")
	        # self.Label4.configure(text='''ENTER NUMBER OF GUEST''')

	        # self.Entry4 = Entry()
	        # self.num=StringVar()
	        # self.Entry4.place(relx=0.40, rely=0.61,height=34, relwidth=0.15)
	        # self.Entry4.configure(background="white")
	        # self.Entry4.configure(disabledforeground="#bfbfbf")
	        # #self.Entry4.configure(font=font10)
	        # self.Entry4.configure(foreground="#000000")
	        # self.Entry4.configure(highlightbackground="#ffffff")
	        # self.Entry4.configure(highlightcolor="black")
	        # self.Entry4.configure(insertbackground="black")
	        # self.Entry4.configure(selectbackground="#e6e6e6")
	        # self.Entry4.configure(selectforeground="black")
	        # self.Entry4.configure(textvariable=self.num)

	        # self.Button3 = Button()
	        # self.Button3.place(relx=0.55, rely=0.61, height=33, width=43)
	        # self.Button3.configure(activebackground="#ffffff")
	        # self.Button3.configure(activeforeground="#000000")
	        # self.Button3.configure(background="#ffffff")
	        # self.Button3.configure(text='''OK''')
	        # self.Button3.configure(command=chk_mo)

	        root.mainloop()

if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT()
        