'''SQL语句参数化'''
import pymysql

# 1.创建与数据库连接对象
db = pymysql.connect(host="localhost", user="root",
                     password="ljk1103", database="db4",
                     charset="utf8")
# 2.利用db方法创建游标对象
cur = db.cursor()
id = input("请输入序号：")
s_id = input("请输入省编号：")
name = input("请输入省名词：")

try:
    sql_insert ="insert into sheng(id, s_id,s_name) " \
                "values(%s, %s,%s);"
    cur.execute(sql_insert, [id, s_id, name])
    print("ok")
    db.commit()
except Exception as e:
    db.rollback()
    print("Failed", e)

cur.close()
db.close()