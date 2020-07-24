import pymysql

# 1.创建与数据库连接对象
db = pymysql.connect(host="localhost", user="root",
                     password="ljk1103", database="db4",
                     charset="utf8")
# 2.利用db方法创建游标对象
cur = db.cursor()
# 3.利用游标对象的execute（）方法执行sql命令
cur.execute("insert into sheng value(16,300000,'台湾省');")
cur.execute("insert into sheng value(1,20000,'北京市');")
cur.execute("insert into sheng value(2,250000,'甘肃省');")
cur.execute("insert into sheng value(7,100000,'西藏自治区');")
cur.execute("insert into sheng value(16,300000,'台湾省');")
# 4.提交到数据库执行
db.commit()
# 5.关闭游标数据
cur.close()
# 6.断开数据库连接
db.close()
