import mysql.connector

#删除记录
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ljk1103",
    database="runoob_db"
)
mycursor = mydb.cursor()
'''
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")
'''
#为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
sql = "DELETE FROM sites WHERE name = %s"
na = ("Taobao",)
mycursor.execute(sql, na)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")