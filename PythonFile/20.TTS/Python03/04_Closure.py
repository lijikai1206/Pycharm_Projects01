#闭包函数示例1:
def make_power(y):
    def fx(arg):
        return arg**y
    return fx
"""
pow2 = make_power(2)
print('3的平方是：',pow2(3))
pow3 = make_power(3)
print('4的立方是：',pow3(4))
"""
#示例2：用参数返回相应的数学函数的示例
#y = a*x**2+b*x+c
def make_function(a, b,c):
    def fx(x):
        return a*x**2+b*x+c
    return fx

fx1 = make_function(4,5,6)
print(fx1(2))

