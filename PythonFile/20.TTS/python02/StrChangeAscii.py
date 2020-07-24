# Filename : test.py
# author by : www.runoob.com

s = "Hello world!"
print(s,type(s))
m2 = ''.join(str(ord(c)) for c in s)
print(m2, type(m2))
str1 = s.encode(encoding='ascii')
print(str1,type(str1))
# while True:
#     # 用户输入字符
#     c = str(input("请输入一个字符: "))
#
#     # 用户输入ASCII码，并将输入的数字转为整型
#     # a = int(input("请输入一个ASCII码: "))
#
#     print(c + " 的ASCII 码为", ord(c))
#     # print(a, " 对应的字符为", chr(a))
