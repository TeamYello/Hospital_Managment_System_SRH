from tkinter import mainloop
from tkinter.constants import E
import pymongo
from pymongo import MongoClient

client = MongoClient(port=27017)

med_name = input("enter the med name")
db = client["Pharma_Medstock"]
col = db["medicine"]

myquery = { "MED_NAME": med_name }

mydoc = col.find(myquery)

for x in mydoc:
  if x ['MED_NAME'] == med_name:
      print(x)
      break
  else:
      print("med doesnt exist")



