# 此示例示意反向算术运算符的重载
class Mylist:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __add__(self, rhs):
        return Mylist(self.data + rhs.data)

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __mul__(self, rhs):
        return Mylist(self.data * rhs)

    def __rmul__(self, lhs):
        print("__rmul__被调用")
        return Mylist(self.data * lhs)

    def __iadd__(self, rhs):
        print("__iadd__被调用")
        self.data.extend(rhs.data)
        return self


L1 = Mylist([1, 2, 3])
L2 = Mylist([4, 5, 6])
L1 += L2
print(L1)
# L3 = L1 + L2    # 等同于L1.__add__(L2)
# print(L3)
# L4 = L2 + L1
# print(L4)
# L5 = L1 * 2
# print(L5)