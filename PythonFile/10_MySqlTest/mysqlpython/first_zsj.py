import pymysql

# 1.创建与数据库连接对象
db = pymysql.connect(host="localhost", user="root",
                     password="ljk1103", database="db4",
                     charset="utf8")
# 2.利用db方法创建游标对象
cur = db.cursor()
# 3.执行sql语句
# 在sheng表中插入1条记录，云南省
try:
    sql_insert = "insert into sheng values(17,300001,'云南省');"
    cur.execute(sql_insert)
    # 把云南省的id号改为666
    sql_update = "update sheng set id=666 where id=17"
    #cur.execute(sql_update)
    # 把台湾省在省表中删除
    sql_delete = "delete from sheng where s_name='台湾省';"
    cur.execute(sql_delete)
    print("ok!")
    # 4.提交到数
    # 据库执行
    db.commit()
except Exception as e:
    db.rollback()
    print("出现错误，已滚回", e)

# 5.关闭游标对象
cur.close()
# 6.断开数据库连接
db.close()