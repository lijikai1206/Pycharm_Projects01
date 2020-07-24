###最小二乘法试验###
#error是自定义计算误差的函数，k,b也就是p0是计算初始化值，args是error其余的参数，该函数返回2个值，第一个是k,b的值
import numpy as np
from scipy.optimize import leastsq

###采样点(Xi,Yi)###
Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78,7.9])
Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05,5.6])

###需要拟合的函数func及误差error###
def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y,s):
    print (s)
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

#TEST
p0=[100,2]
s="Test the number of iteration-001"
print( error(p0,Xi,Yi,s))

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
k,b=Para[0]
print("k=",k,'\n',"b=",b)

###绘图，看拟合效果###
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()