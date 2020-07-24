#!/usr/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
'''
myquery = {"name": "RUNOOB"}
mycol.delete_one(myquery)
# 删除后输出
for x in mycol.find():
    print(x)

#删除集合中的多个文档
#myquery = {"name": {"$regex": "^F"}}
myquery = {"name": "Github"}
x = mycol.delete_many(myquery)
print(x.deleted_count, "个文档已删除")
for x in mycol.find():
    print(x)

#删除所有文档
x = mycol.delete_many({})
print(x.deleted_count, "个文档已删除")
'''
#删除集合
mycol.drop()