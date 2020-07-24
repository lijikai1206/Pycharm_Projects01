import numpy as np
a = np.arange(0,12,0.5).reshape(4,-1)
print(a)
np.savetxt('a.txt',a)                          #默认按照'%.18e’格式保存数据，以空格分割
np.savetxt('a1.txt',a,fmt='%f',delimiter=',')   #更改保存为整数
txt = np.loadtxt('a.txt')
txt1 = np.loadtxt('a1.txt',delimiter=',')
print(txt1)
