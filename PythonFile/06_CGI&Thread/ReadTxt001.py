# coding: utf-8
import re
d = "[\u4e00-\u9fa5]+" #中文匹配的符号
path = r'D:\Python\05Example\\test001.txt'
with open(path, 'rb') as f:
    content = f.read()
    print(f)
    print(content)
    L = []
    for i in f:
        i = i.decode('utf-8')
        I = re.findall(d, i)
        L += I
    print(L)
