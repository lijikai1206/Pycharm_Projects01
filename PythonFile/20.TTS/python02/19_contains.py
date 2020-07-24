# 此例示意一元运算符的重载
class Mylist:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __contains__(self, item):
        '''此方法用来实现in / not in 运算符的重载'''
        print("__contains__被调用")
        for x in self.data:
            if x == item:
                return True
        return False


L1 = Mylist([1, -2, 3, -4])
if -2 in L1:
    print('-2 在 L1 中')
else:
    print('-2 不在L1中')

if -3 not in L1:
    print("-3 不在L1中")
else:
    print("-3在L1中")