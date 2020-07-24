# 此例示意类方法的定义方法和用法

class Car:
    count = 0  # 类变量

    @classmethod
    def getTotalCount(cls):
        '''此方法为类方法，第一个参数为cls，代表调用此方法的类'''
        return cls.count

    @classmethod
    def updateCount(cls, number):
        cls.count += number

print(Car.getTotalCount())      # 用类来调用类方法
Car.updateCount(2)              # m面向对象思想不提倡直接操作属性，定义类方法实现
print(Car.getTotalCount())


