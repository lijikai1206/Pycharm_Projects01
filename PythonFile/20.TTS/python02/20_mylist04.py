# 此例示意 [] 运算符的重载
class Mylist:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __getitem__(self, item):
        print("__getitem__被调用")
        if type(item) is int:
            print("正在做索引操作")
        elif type(item) is slice:
            print("正在做切片操作")
            print("切片的起始值：", item.start)
            print("切片的终止值：", item.stop)
            print("切片的步长：", item.step)
        else:
            raise TypeError
        return self.data[item]

    def __setitem__(self, key, value):
        print("__setitrm__被调用, key =", key, "value = ", value)
        self.data[key] = value      # 修改data绑定的列表


L1 = Mylist([1, -2, 3, -4,5, -6])
print(L1[::2])



# L1[1] = 2     # 等同于调用L1.__setitem__(1, 2)
# print(L1)

# 以下操作会出错
# print(L1[1000])
# print(L1['hello'])