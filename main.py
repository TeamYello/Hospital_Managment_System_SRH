

import csv

# Define global variables
patient_fields = ['Patient_ID', 'Patient_Name', 'Room_No', 'Age', 'Phone']
patient_database = 'patient.csv'

'''
Function name: display_menu
Overview of this function:
1) Welcome the user in terminal
2) Ask for their desire choice
'''

def display_menu():   # Represents the main area or dashboard for hospital

    print("1. Billing")
    print("2. Quit")



def Billing():
    import read
    import purchase
    import write


    print("-------------------------------")
    print(" Thank you for using our system")
    print("-------------------------------")

    again="Y"
    while again.upper()=="Y":
        a=read.medicine()
        b=purchase.purchase(a)
        write.over_write(a,b)
        again=input("\nDoes the any new customer waiting to buy product? ")
        print("\nThank you for shopping from our store!!")
        print("Please check your invoice for your shopping details, \nWhich we created txt file format for you.")


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        Billing()
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")

