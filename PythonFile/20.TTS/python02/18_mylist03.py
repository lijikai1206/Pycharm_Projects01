# 此例示意一元运算符的重载
class Mylist:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __neg__(self):
        '''此方法用来指定 - self 返回的规则'''
        # L = [-x for x in self.data]
        L = (-x for x in self.data)
        return Mylist(L)


L1 = Mylist([1, -2, 3, -4])
L2 = -L1
print(L2)