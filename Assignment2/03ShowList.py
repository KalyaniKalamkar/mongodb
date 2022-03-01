# Write a program to show list of all documents from the collection

import pymongo
from pymongo import MongoClient
import urllib.parse

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]

for dic in coll.find():
    print(list(dic.values()))