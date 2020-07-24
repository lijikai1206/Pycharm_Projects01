import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
'''
myquery = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}
mycol.update_one(myquery, newvalues)
# 输出修改后的  "sites"  集合
for x in mycol.find():
    print(x)
'''
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "文档已修改")