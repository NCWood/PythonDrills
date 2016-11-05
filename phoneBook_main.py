#===========================================================])
# Python Version: 3.5.2                                     |)
#                                                           |)
# Python/Tkinter Phonebook Drill                            |)
#                                                           |)
# Author: The Tech Academy                                  |)
#                                                           |)
# Co-Author: N.C.Wood (nicholas.cameron.wood@gmail.com)     |)
#                                                           |)
# This code was written and tested to work with Windows 10  |)
#                                                           |)
#===========================================================])

from tkinter import *
import tkinter as tk

import phoneBook_gui
import phoneBook_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, *kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        phoneBook_func.center_window(self,500,300)
        self.master.title("Python & Tkinter Phonebook")
        self.master.configure(bg = '#8cb3db')

        self.master.protocol("WM_DELETE_WINDOW", lambda: phoneBook_func.ask_quit(self))
        arg = self.master

        phoneBook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        
        

