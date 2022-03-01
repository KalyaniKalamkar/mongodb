# Write a program to accept ID, ram and rom. Update the document with new ram and rom of the model. 

import pymongo
from pymongo import MongoClient
import urllib.parse

code=input("Enter Id :")
qr={}
qr["ID"]=code
print(qr)

ram=int(input("Enter RAM : "))
ch={}
ch["RAM"]=ram

print(ch)

ram=int(input("Enter ROM : "))
ck={}
ck["ROM"]=ram
print(ck)

upd={"$set":ch}
upd2={"$set":ck}

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]


coll.update_one(qr,upd)
print("RAM Updated Successfully!!")

coll.update_one(qr,upd2)
print("ROM Updated Successfully!!")