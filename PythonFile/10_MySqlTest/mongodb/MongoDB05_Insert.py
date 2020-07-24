#!/usr/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

#集合中插入文档使用 insert_one() 方法，该方法的第一参数是字典 name => value 对。
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)
print(x)
print(x.inserted_id)

mylist2 = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
y = mycol.insert_many(mylist2)
# 输出插入的所有文档对应的 _id 值
print(y)
print(y.inserted_ids)
