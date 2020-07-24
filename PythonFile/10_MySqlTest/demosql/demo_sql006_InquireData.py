import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ljk1103",
    database="runoob_db"
)
mycursor = mydb.cursor()
'''#1.查询数据
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)

#2.读取指定的字段数据
mycursor.execute("SELECT name, url FROM sites")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#3.只读取一条数据，可以使用 fetchone() 方法
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchone()
print(myresult)

#4.使用 where 语句，读取指定条件的数据。也可以用通匹符%。
sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
#5.为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)
mycursor.execute(sql, na)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)