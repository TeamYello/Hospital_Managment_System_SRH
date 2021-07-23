import pymongo
from bson import ObjectId
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["shift"]
mycol3 = mydb["shift_plan4"]
mycol4 = mydb["alternate_shift_plan"]


# Check DB with date criteria
# for x in mycol3.find({"Date":"25-07-2021"},{ "_id": 0, "First_Name": 1,"Last_Name":1,"Shift":1,"Status":1}):
#     print(x)

1.#Nurse enters details of unavailability in the system

def insert_data(data):
    
    document = mycol3.insert_one(data)
    return document.inserted_id

#2. Service manager to check all records for particular date
# for z in mycol3.find():
#     print(z)

#3.Check for unavailability records
# for x in mycol3.find({"Status":"UA"},{ "_id": 0, "First_Name": 1,"Last_Name":1,"Shift":1,"Status":1}):
#          print(x)

#4.Check for alternate records available for duty for particular date
mycol4=mydb["alternate_shift_plan"]
# for z in mycol3.find({"Date":"25-07-2021"},{ "_id": 0, "First_Name": 1,"Last_Name":1,"Shift":1,"Status":1,"phone":1}):
#     print(z)

#5.Update many records of stand by nurse for particular date

def insert_manydata(data1):
    
    document = mycol4.insert_many(data1)
    return document.inserted_ids

#6.Service manager to update nurse from available to unavailable

def update_existing(filter, data):
    
    document = mycol3.update_one(filter, {"$set": data})
    return document.acknowledged

#7. Delete nurse record

def remove_data(delete):
    document = mycol4.delete_one(delete)
    return document.acknowledged
    
1.#Nurse enters details of unavailability in the system

# data = {"_id": "14", "First_Name": "Venkat", "Last_Name": "Sharma", "Date_of_Birth": "27-09-1997","e_mail":"venkat@gmail.com","phone":"9987465220","In_time":"06:00","out_time":"14:00","Shift":"First_shift","Date":"20-07-2021","Status":"UA"}
# insert_data(data)
# print("Data inserted")

#5.Update many records of stand by nurse for particular date

# data1=[
# {"_id": "6", "First_Name": "Rahul", "Last_Name": "Ajit", "Date_of_Birth": "22-08-1994","e_mail":"rahul@gmail.com","phone":"8594039275","In_time":"22:00","out_time":"06:00","Shift":"Third_shift","Date":"25-07-2021","Status":"A"},
# {"_id": "7", "First_Name": "Majur", "Last_Name": "Joshi", "Date_of_Birth": "14-09-1990","e_mail":"mayur@gmail.com","phone":"8594003395","In_time":"14:00","out_time":"22:00","Shift":"Second_shift","Date":"25-07-2021","Status":"A"}
# ]

# insert_manydata(data1)
# print(data1)

#6. Service manager to update nurse shift details as per their availability 

filter={"_id":"13"}
data={'Shift':'Third_shift'}

# updatedrecord=update_existing(filter,data)
# print(updatedrecord)

#7. Delete nurse record

delete={"_id":"7"}
deletedrecord=remove_data(delete)
print(deletedrecord)







