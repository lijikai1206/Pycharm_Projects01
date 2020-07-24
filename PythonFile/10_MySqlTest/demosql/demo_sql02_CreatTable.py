import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ljk1103",
    database="runoob"
)
mycursor = mydb.cursor()

#创建数据表
mycursor.execute("CREATE TABLE Websites (id VARCHAR(255), "
                 "name VARCHAR(255), url VARCHAR(255),alexa VARCHAR(255),"
                 "country VARCHAR(255))")

#查看数据表是否已存在。
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)