
fileName = r'D:\Python\05Example\log02.txt'
str = 'Name:Lee Jack(李吉凯) \nPhoneNumber（手机号码）:13600173445\n'       #str类型
mem = str.encode('gbk').decode('iso-8859-1')         #byte类型

with open(fileName,'w', encoding='iso-8859-1') as f:
    f.write(mem)
    print('写入成功！')


