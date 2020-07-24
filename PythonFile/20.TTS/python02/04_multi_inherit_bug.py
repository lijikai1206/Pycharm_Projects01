# 小张写了一个类A
class A:
    def m(selfs):
        print("A.m()被调用")

# 小李写了一个类B
class B:
    def m(self):
        print('B.m()被调用')

# 小王感觉小张和小李的两个类自己可以用
class AB(B, A):
    pass

ab = AB()
ab.m()   # 只有  B.m()被调用 !!!!!!!!!!!!!