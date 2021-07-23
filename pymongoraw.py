import pymongo
from tkinter import *
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import Button
import sys
from tkinter import messagebox
from tkinter import Entry, Label, Toplevel
from pymongo import MongoClient

try:
   client = MongoClient(port=27017)
   db=client.DiseasePrediction
   print("Connected to MongoDB")
except :
	print("Database connection Error ")
	print("No connection could be made because the target machine actively refused it ")
	messagebox.showerror("Error", "Connection Error")
	sys.exit()


file=pd.read_csv("file22.csv")
#tr=pd.read_csv("file2")#testing purpose



def add_Symptoms():
        symptoms = Symptom1.get()
        Disease = Symptom2.get()
        
        Disease_Name=[Disease]
        symptomsType=[symptoms]

        if len(symptoms)==0 and db.symptoms.count_document(limit=1)==0:
            messagebox.showwarning("WARNING", "All fields are compulsory")
            return
        if len(Disease)==0 and db.Disease.count_documents(limit=1)==0:
            messagebox.showwarning("WARNING","All Fields are compulsory")   
        elif len(symptoms)!=0 and db.symptoms.count_documents( limit = 1)==0:
            result=db.DiseasePrediction.insert_one(Disease)    
        else:
             messagebox.showwarning("ERROR")
             return

   
root=Tk()
root.configure(background="black")

Symptom1 = StringVar()
Symptom1.set("Select Here")

Symptom2 = StringVar()
Symptom2.set("Select Here")

Symptom3 = StringVar()
Symptom3.set("Select Here")

Symptom4 = StringVar()
Symptom4.set("Select Here")

Symptom5 = StringVar()
Symptom5.set("Select Here")

Name = StringVar()

w2 = Label(root, justify=LEFT, text="Disease Predictor ", fg="Red", bg="White")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb = Label(root, text="Name of the Patient", fg="Red", bg="Sky Blue")
NameLb.config(font=("Times",15,"bold italic"))
NameLb.grid(row=6, column=10, pady=30 ,sticky=W)

S1Lb = Label(root, text="Symptom 1")

S2Lb = Label(root, text="Symptom 2")

S3Lb = Label(root, text="Symptom 3")

S4Lb = Label(root, text="Symptom 4" )

S5Lb = Label(root, text="Symptom 5")

OPTIONS = sorted(file)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=1)

dst = Button(root, text="New Symptom",command=lambda: add_Symptoms(root,db))
search=Button(root,text='search for medicine',command=lambda :"newone"(root,db))

root.mainloop()