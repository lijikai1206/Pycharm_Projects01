from pymysql import *

class Mysqlpython:
    def __init__(self,database,
                 host="localhost",
                 user="root",
                 password="ljk1103",
                 port="3306",
                 charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        print(self.password)
        self.port = port
        self.charset = charset
        self.database = database
        print("初始化方法执行完毕！")

    def open(self):
        print("begin link connect sql")
        self.db = connect(host=self.host,
                          user=self.user,
                          port=self.port,
                          password=self.password,
                          database=self.database,
                          charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self, sql, L=[]):
        try:
            self.open()
            self.cur.execute(sql, L)
            self.db.commit()
            print("ok")
        except Exception as e:
            self.db.rollback()
            print("Failed", e)
        self.close()

    def all(self, sql, L=[]):
        try:
            self.open()
            print("open方法执行")
            self.cur.execute(sql,L)
            print("execute方法执行")
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("Failed", e)
        self.close()

if __name__ == "__main__":
    sqlh = Mysqlpython("db4")
    sql_select = "select * from sheng where id=%s;"
    data = sqlh.all(sql_select, [1])
    print(data)