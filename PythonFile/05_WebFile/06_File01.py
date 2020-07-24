import os
'''
name = os.name
print(name)
environ = os.environ
print(environ)
content = str(environ)
with open('environ.txt', 'w') as f:
    f.write(content)
path = os.environ.get('PATH')
print(path)
'''
path1 = os.path.abspath('.')
print(path1)
path2 = os.path.join(path1,'testdir')
print(path2)
#os.mkdir(path2)
#os.rmdir(path2)
os.rename('environ.txt', 'environ123.txt') 