#Write a program to accept ID and new price of the mobile. Update the document with new price. Display the document after updating.

import pymongo
from pymongo import MongoClient
import urllib.parse

code=input("Enter Id :")
qr={}
qr["ID"]=code
print(qr)

price=float(input("Enter Price : "))
ch={}
ch["Price"]=price

print(ch)

upd={"$set":ch}

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]


coll.update_one(qr,upd)
print("Mobile Price Updated Successfully!!")