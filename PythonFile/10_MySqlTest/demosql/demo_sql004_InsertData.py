import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ljk1103",
    database="runoob"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Websites (id, name, url, alexa, country) VALUES (%s, %s, %s, %s,%s)"
val = [
    ('1','Google', 'https://www.google.com','1','USA'),
    ('2','Github', 'https://www.github.com','13','CN'),
    ('3','Taobao', 'https://www.taobao.com','4689','CN'),
    ('4','stackoverflow', 'https://www.stackoverflow.com/','20','USA')
]

mycursor.executemany(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")