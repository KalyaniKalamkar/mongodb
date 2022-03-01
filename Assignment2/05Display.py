# Write a program to take company as an input and display documents of all mobiles of the company

import pymongo
from pymongo import MongoClient
import urllib.parse

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]

code=input("Enter Company :")
qr={}
qr["Company"]=code
print(qr)

for doc in coll.find(qr):
    print(doc)
