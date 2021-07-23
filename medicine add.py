from __future__ import unicode_literals
from re import L, search
from tkinter import Entry, Label, Toplevel
from dns.rdatatype import EUI64

from pymongo import MongoClient
from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Button
import sys

try:
	client = MongoClient(port=27017)
	db=client.Pharma_Medstock
	print("Connected to MongoDB")
except :
	print("Database connection Error ")
	print("No connection could be made because the target machine actively refused it ")
	messagebox.showerror("Error", "Connection Error")
	sys.exit(1)
	


root=Tk()
root.geometry('600x600')
root.title("Pharma Management System")

def add_med(root,db): 
    def add_query():
        global root
        med_name = E1.get()
        type_ = E2.get()
        issuedate = E3.get()
        expdate = E4.get()
        price = E5.get()
        ref_no = E.get()


        
        MED_NAME = [med_name]
        TYPE = [type_]
        ISSUE_D = [issuedate]
        EXP_D = [expdate]
        PRICE = [price]
        REFNO = [ref_no]

        Pharma_Medstock = {  
        'MED_NAME' : MED_NAME[randint(0, (len(MED_NAME)-1))] ,
        'TYPE' : TYPE[randint(0, (len(TYPE)-1))],
        'ISSUE_D' : ISSUE_D[randint(0, (len(ISSUE_D)-1))],
        'EXP_D' : EXP_D[randint(0, (len(EXP_D)-1))],
        'PRICE' : PRICE[randint(0, (len(PRICE)-1))],
        'REFNO' : REFNO[randint(0, (len(REFNO)-1))] }
        
        if(len(med_name)==0):
            messagebox.showwarning("WARNING", "All fields are compulsory")
            return
        if(len(type_)==0):
            messagebox.showwarning("WARNING", "All fields are compulsory")
            return
        if(len(issuedate)==0):
            messagebox.showwarning("WARNING", "All fields are compulsory")
            return
        if(len(expdate)==0):
            messagebox.showwarning("WARNING", "All fields are compulsory")
            return
        if(len(price)==0):
            messagebox.showwarning("WARNING", "All fields are compulsory")
            return
        if len(ref_no)==0 and db.medicine.count_documents({ 'REFNO': ref_no }, limit = 1)==0:
             result=db.medicine.insert_one({'REFNO':ref_no,'MED_NAME':med_name, 'TYPE':type_ ,'ISSUE_D': issuedate, 'EXP_D': expdate,'PRICE':price})
        elif len(ref_no)!=0 and db.medicine.count_documents({ 'REFNO': ref_no }, limit = 1)==0:
             result=db.medicine.insert_one(Pharma_Medstock)
        else:
             messagebox.showwarning("ERROR", "MEDICINE Already Exists")
             return
       	
        newwin.destroy()
        messagebox.showinfo("Add Medicine", "Medicine Added")
    newwin = Toplevel(root)
    newwin.geometry('600x600')
    newwin.title("Add MEDICINE")
    L1 = Label(newwin, text="MEDICINE NAME")
    L1.place(x=10,y=50)
    E1 = Entry(newwin, bd=7)
    E1.place(x=100,y=50)
    L2 = Label(newwin, text="TYPE")
    L2.place(x=10,y=100)
    E2 = Entry(newwin, bd=7)
    E2.place(x=100,y=100)
    L3 = Label(newwin, text="ISSUE DATE")
    L3.place(x=10,y=150)
    E3 = Entry(newwin, bd=7)
    E3.place(x=100,y=150)
    L4 = Label(newwin, text="EXP DATE")
    L4.place(x=10,y=200)
    E4 = Entry(newwin, bd=7)
    E4.place(x=100,y=200)
    L5 = Label(newwin, text="PRICE")
    L5.place(x=10,y=250)
    E5 = Entry(newwin, bd=7)
    E5.place(x=100,y=250)
    L = Label(newwin, text="REFNO")
    L.place(x=10,y=300)
    E = Entry(newwin, bd=7)
    E.place(x=100,y=300)
    sub=Button(newwin,text="ADD",command=add_query)
    sub.place(x=120,y=350)


add= Button(root,text='Add New Medicine',command=lambda :add_med(root,db))
add.place(x=100,y=100)
root.mainloop()