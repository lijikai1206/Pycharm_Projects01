#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydoc = mycol.find().sort("alexa",-1)  #-1表示降序排序。
for x in mydoc:
    print(x)