import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ljk1103",
    database="runoob_db"
)
mycursor = mydb.cursor()

#1.按 name 字段字母的升序排序：
#sql = "SELECT * FROM sites ORDER BY name"
#2.按 name 字段字母的降序排序：
#sql = "SELECT * FROM sites ORDER BY name DESC"
#3.通过 "LIMIT" 语句来指定查询的数据
#sql = "SELECT * FROM sites LIMIT 3"
#4.指定起始位置，使用的关键字是 OFFSET
#sql = "SELECT * FROM sites LIMIT 3 OFFSET 1"# 0 为 第一条，1 为第二条，以此类推

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)