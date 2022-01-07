import os

class Contact:
    def __init__(self,first_name=None,last_name=None,address=None,city=None,state=None,zip=0,phone_number=0,email=None):
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

myContact = Contact()
print(str(myContact))

