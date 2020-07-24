# 多态
class Shape:
    def draw(self):
        print("Shape.draw被调用。")
class Point(Shape):
    def draw(selfs):
        print('正在画一个点。')

class Circle(Point):
    def draw(selfs):
        print('正在画一个圆。')

def my_draw(s):
    s.draw()     # 此处显示多态中的动态

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)
