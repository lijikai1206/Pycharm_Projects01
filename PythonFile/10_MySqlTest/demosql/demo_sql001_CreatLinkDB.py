import mysql.connector
'''
#创建数据库连接
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="ljk1103"  # 数据库密码
)
print(mydb)
'''
#创建数据库
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="ljk1103"  # 数据库密码
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE TESTDB")  #只能创建一次，存在就不用重复创建了，否则会报错。
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)