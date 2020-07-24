# 此例示范 类的变量 __slots__ 列表的作用

class Students:
    __slots__ = ['name', 'score']
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Students('小张', 58)
print(s1.score)
# s1.socre = 100   # 当没有 __slots__ 时，此处写错了属性名，但运行是不会报错
s1.score = 100
print(s1.score)