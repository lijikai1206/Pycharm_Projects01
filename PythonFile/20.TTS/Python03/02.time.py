import time

#计算出生的日期
year = int(input("输入年："))
month = int(input("输入月："))
day = int(input("输入日："))

#得到出生的秒数
birthday_second = time.mktime((year, month,day,0,0,0,0,0,0))
print(birthday_second)
#得到当前时间的描述
cur_second = time.time()
print(cur_second)
#(1).计算你已经出生了多少天？
s = cur_second - birthday_second
print(s)
days = s/60/60//24
print("你已经出生：",days)

#(2)计算你出生的那天是星期几？
birday = (year, month, day,0,0,0,0,0,0)
s = time.mktime(birday)
t = time.localtime(s)
weekday = {0:"星期一",1:"星期二",2:"星期三",3:"星期四",5:"星期五",6:"星期六"}
print("你出生的那天是：", weekday[t[6]])


