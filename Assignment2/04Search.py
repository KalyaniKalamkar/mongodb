#Write a program to take ID as input, search and display the document with mobile information

import pymongo
from pymongo import MongoClient
import urllib.parse

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]

code=input("Enter Id :")
qr={}
qr["ID"]=code
print(qr)

for doc in coll.find(qr):
    print(doc)
