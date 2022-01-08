'''
@Author: Hitesh Patil
@Date: 08-01-2022 11:05:46
@Last Modified by: Hitesh Patil
@Last Modified time: 08-01-2022 16:00:00
@Title : AddressBook System - Adding New Contact
'''

import os

class Address_Book:
    #Constructor With Arguments
    def __init__(self,first_name=None,last_name=None,address=None,city=None,state=None,zip=0,phone_number=0,email=None):
        #set Variable
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phone_number=phone_number
        self.email=email
        
    def __str__(self):
        return "First Name:{0}\nLast Name:{1}\nAddress:{2}\nCity:{3}\nState:{4}\nZip:{5}\nPhone Number:{6}\nEmail:{7}".format(self.first_name,self.last_name,self.address,self.city,self.state,self.zip,self.phone_number,self.email)

# myContact = Address_Book()
# print(str(myContact))
    def __str__(self):
      return f"{self.first_name} {self.last_name} : {self.address} : {self.city} : {self.state} : {self.zip} : {self.phone_number} : {self.email}"

print("Enter new Contact Detail on Below\n")
first_name=input("Enter First Name: ")
last_name=input("Enter  Last Name: ")
address=input("Enter Address: ")
city=input("Enter City: ")
state=input("Enter state: ")
zip=input("Enter Zip Code: ")
phone_number=input("Enter Phone Number: ")
email=input("Enter Email: ")


our_contact=Address_Book(first_name,last_name,address,city,state,zip,phone_number,email)
print("\n",our_contact)
print("\nContact Added Successfuly")

exit