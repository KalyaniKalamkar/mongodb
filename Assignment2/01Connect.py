from pymongo import MongoClient
import pymongo
import urllib.parse

try:
    username=urllib.parse.quote_plus('kalyani')
    password=urllib.parse.quote_plus('Kalyani@123')
    client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
    db=client['shopping']
    coll=db["mobile"]
    print("connected successfully!!")
except:
    print("Sorry!connection failed!!")