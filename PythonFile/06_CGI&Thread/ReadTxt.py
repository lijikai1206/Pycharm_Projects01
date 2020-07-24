import chardet

File = r'D:\Python\05Example\log02.txt'
f = open(File, 'rb')
data = f.read()
Encode = chardet.detect(data).get('encoding')
print(Encode)
print(data)
#uft_str = str.encode("iso-8859-1").decode('gbk').encode('utf8')

f1 = open(File,'r').read()#.encode(Encode).decode('gbk')
print(f1)