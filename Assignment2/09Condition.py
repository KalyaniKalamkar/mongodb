# Write a program to accept price and display all documents having price less than the input value

import pymongo
from pymongo import MongoClient
import urllib.parse

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]

code=float(input("Enter Price:"))

myquery={"Price":{"$lt":code}}
mydoc=coll.find(myquery)

print("Documents having price less than the input value are :")
for x in mydoc:
    print(x)
