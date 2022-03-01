 #Write a program to accept ID, fetch the document from collection, copy it in another collection "outofstock" and delete the document from the "mobiles" collection

import pymongo
from pymongo import MongoClient
import urllib.parse

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]
co=db["outofstock"]

code=input("Enter Id :")
qr={}
qr["ID"]=code
print(qr)

for doc in coll.find(qr):
    print(doc)
    co.insert_one(doc)
    coll.delete_one(doc)

    print("Document Copied and Deleted Successfully!!")


