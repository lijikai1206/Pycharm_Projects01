#!/usr/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
'''
#x = mycol.find_one()
#2.查询集合中所有的数据
for x in mycol.find():
    print(x)

#3.查询指定字段的数据
for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }):
  print(x)

#4.根据指定条件查询
myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

#5.高级查询。用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
myquery = {"name": {"$gt": "H"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

#6.使用正则表达式查询
myquery = {"name": {"$regex": "^R"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
'''
#7.返回指定条数记录
myresult = mycol.find().limit(3)
# 输出结果
for x in myresult:
    print(x)