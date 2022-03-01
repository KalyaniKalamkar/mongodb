#Write a python program to take input from the user and add employee data as a document in the collection (ex. ID, company, model,processor, screensize, ram, rom, connectivity, price, rating, etc.)

from pymongo import MongoClient
import pymongo
import urllib.parse

id=input("Enter ID : ")
com=input("Enter company name : ")
mod=input("Enter model name : ")
bat=int(input("Enter Battery (mAh) : "))
ss=float(input("Enter Screensize (inch) : "))
ram=int(input("Enter RAM : "))
rom=int(input("Enter ROM : "))
price=float(input("Enter Price : "))
rating=float(input("Enter Rating : "))

dic={}
dic["ID"]=id
dic["Company"]=com
dic["Model"]=mod
dic["Battery"]=bat
dic["ScreenSize"]=ss
dic["RAM"]=ram
dic["ROM"]=rom
dic["Price"]=price
dic["Rating"]=rating

username=urllib.parse.quote_plus('kalyani')
password=urllib.parse.quote_plus('Kalyani@123')
client=MongoClient("mongodb+srv://{}:{}@cluster0.vqcqh.mongodb.net/shopping?retryWrites=true&w=majority".format(username,password))
db=client['shopping']
coll=db["mobile"]

coll.insert_one(dic)
print("New mobile added to cloud MongoDB Collection")


