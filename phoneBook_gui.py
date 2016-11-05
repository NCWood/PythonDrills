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

import phoneBook_main
import phoneBook_func


def load_gui(self):

    #Labels======================================================================
    self.label_fname = tk.Label(self.master, text = 'First Name:', bg = '#8cb3db')
    self.label_lname = tk.Label(self.master, text = 'Last Name:', bg = '#8cb3db')   
    self.label_phone = tk.Label(self.master, text = 'Phone Number:', bg = '#8cb3db')
    self.label_email = tk.Label(self.master, text = 'Email Address:', bg = '#8cb3db')       
    self.label_info = tk.Label(self.master, text = 'Information:', bg = '#8cb3db')            
                                                                            
    self.label_fname.grid(row = 0, column = 0, padx=(27,0), pady=(10,0), sticky = 'nw')
    self.label_lname.grid(row = 2, column = 0, padx=(27,0), pady=(10,0), sticky = 'nw')
    self.label_phone.grid(row = 4, column = 0, padx=(27,0), pady=(10,0), sticky = 'nw')
    self.label_email.grid(row = 6, column = 0, padx=(27,0), pady=(10,0), sticky = 'nw')
    self.label_info.grid(row = 0, column = 2, padx=(27,0), pady=(10,0), sticky = 'nw')
    #================================================================================

    #Entries===========================================
    self.entry_fname = tk.Entry(self.master, text = '')
    self.entry_lname = tk.Entry(self.master, text = '')
    self.entry_phone = tk.Entry(self.master, text = '')
    self.entry_email = tk.Entry(self.master, text = '')

    self.entry_fname.grid(row = 1, column = 0, columnspan = 2, padx=(30,40), pady=(0,0), sticky = 'nw')
    self.entry_lname.grid(row = 3, column = 0, columnspan = 2, padx=(30,40), pady=(0,0), sticky = 'nw')
    self.entry_phone.grid(row = 5, column = 0, columnspan = 2, padx=(30,40), pady=(0,0), sticky = 'nw')
    self.entry_email.grid(row = 7, column = 0, columnspan = 2, padx=(30,40), pady=(0,0), sticky = 'nw')
    #=================================================================================================


    #ListBox and Scrollbars====================================
    self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
    
    self.listbox_info = Listbox(self.master, exportselection = 0, yscrollcommand=self.scrollbar1.set)

    self.listbox_info.bind('<<ListboxSelect>>',lambda event: phoneBook_func.onSelect(self, event))

    self.scrollbar1.config(command = self.listbox_info.yview)

    self.scrollbar1.grid(row = 1, column = 5, rowspan = 7, padx=(0,0), pady=(0,0), sticky = 'nes')
    
    self.listbox_info.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, padx=(0,0), pady=(0,0), sticky = 'nesw')
    #===============================================================================================================

    #Buttons=====================================================================================================================================
    self.button_add = tk.Button(self.master, width = 12, height = 2, text = 'Add', bg = '#6da4db', command=lambda: phoneBook_func.addToList(self))
    self.button_update = tk.Button(self.master, width = 12, height = 2, text = 'Update', bg = '#6da4db', command=lambda: phoneBook_func.onUpdate(self))
    self.button_delete = tk.Button(self.master, width = 12, height = 2, text = 'Delete', bg = '#6da4db', command=lambda: phoneBook_func.onDelete(self))
    self.button_close = tk.Button(self.master, width = 12, height = 2, text = 'Close', bg = '#6da4db', command=lambda: phoneBook_func.ask_quit(self))

    self.button_add.grid(row = 8, column = 0, padx=(25,0), pady=(45,10), sticky = 'w')
    self.button_update.grid(row = 8, column = 1, padx=(15,0), pady=(45,10), sticky = 'w')
    self.button_delete.grid(row = 8, column = 2, padx=(15,0), pady=(45,10), sticky = 'w')
    self.button_close.grid(row = 8, column = 4, padx=(15,0), pady=(45,10), sticky = 'e')
    #==================================================================================

    #Scrollbars===============================================
    self.yscroll = tk.Scrollbar(self.master, orient = VERTICAL)

    self.yscroll.grid(row = 1, column = 5, rowspan = 7, padx=(0,0), pady=(0,0), sticky = 'nes')

    self.yscroll.config(command = self.listbox_info.yview)
    #====================================================


    phoneBook_func.create_db(self)
    phoneBook_func.onRefresh(self)
    




    
if __name__ == "__main__":
    pass



