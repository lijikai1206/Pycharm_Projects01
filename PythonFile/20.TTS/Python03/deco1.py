#此用例示意函数装饰器的用法
#定义一个装饰器函数
def mydeco(fn):
    def fx():
        print('+++++++++++')
        fn()
        print('-----------')
    return fx

@mydeco
def myfunc():
    print("myfun被调用！")

#调用函数的地方可能是其他人写的
myfunc()





