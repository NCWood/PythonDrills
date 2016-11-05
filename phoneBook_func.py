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

import os
from tkinter import *
import tkinter as tk
import sqlite3

import phoneBook_main
import phoneBook_gui

#=============================
def center_window(self, w, h):                                                    
    # get screen width and height                                                 
    screen_width = self.master.winfo_screenwidth()                                
    screen_height = self.master.winfo_screenheight()                              
    # calculate x and y coords to center app                                      
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)
#==================

        
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );""")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur, count

# Select item in listbox
def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""",[value])
        varBody = cursor.fetchall()
        for data in varBody:

            self.entry_fname.delete(0,END)
            self.entry_lname.delete(0,END)
            self.entry_phone.delete(0,END)
            self.entry_email.delete(0,END)


            self.entry_fname.insert(0,data[0])
            self.entry_lname.insert(0,data[1])
            self.entry_phone.insert(0,data[2])
            self.entry_email.insert(0,data[3])
        
            
           

def addToList(self):
    var_fname = self.entry_fname.get()
    var_lname = self.entry_lname.get()
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.entry_phone.get().strip()
    var_email = self.entry_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.listbox_info.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please verify that there is data in all four fields.")


def onDelete(self):
    var_select = self.listbox_info.get(self.listbox_info.curselection())
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", " All information associated with ({}) \nwill be permanently deleted".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)

                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Area", "({}) is the last record in the database and cannot be deleted at this time".format(var_select))
    conn.close()


def onDeleted(self):
    self.entry_fname.delete(0,END)
    self.entry_lname.delete(0,END)
    self.entry_phone.delete(0,END)
    self.entry_email.delete(0,END)

    try:
        index = self.listbox_info.curselection()[0]
        self.listbox_info.delete(index)

    except IndexError:
        pass


def onClear(self):
    self.entry_fname.delete(0,END)
    self.entry_lname.delete(0,END)
    self.entry_phone.delete(0,END)
    self.entry_email.delete(0,END)


def onRefresh(self):
    self.listbox_info.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall() [i]
            for item in varList:
                self.listbox_info.insert(0,str(item))
                i = i +1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.listbox_info.curselection()[0]
        var_value = self.listbox_info.get(var_select)
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return

    var_phone = self.entry_phone.get().strip()
    var_email = self.entry_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for ({}). \nProceed with the update request?".format(var_phone, var_email, var_value))
                
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messageabox.showinfo("Cancel request","No changes have been made to ({})".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in  the database for this name.\n\nYour update request has been cancelled.".format(var_phone, var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)



if __name__ == "__main__":
    pass
                                    
                                                
                                                  
                                                                                                                                                                                  
        

    
    
                                                                                   
    
                                                                                   


                                                        
                                                                                
    
          
    
        



























                                                                                                                                    
                                                                                                                                    






        
