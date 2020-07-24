# 此例实例继承和派生

class Human:
    '''此类用来描述人类的共性行为'''
    def say(self, that):
        print("说", that)
    def walk(self, distance):
        print("走了", distance, "公里")

class Student(Human):
    # def say(self, that):
    #     print(("说", that)
    # def walk(self, distance):
    #     print("走了", distance, "公里")
    def study(self, subject):
        print("正在学习", subject)

class Teacher(Human):
    def teacher(self, subject):
        print("正在教", subject)

        
h1 = Human()
h1.say('今天天气特别热！')
h1.walk(5)

print('-------------以下是学生对象的行为------------')
s1 = Student()
s1.say('学习有点累')
s1.walk(3)
s1.study('Python')

print('-------------以下是老师对象的行为------------')
t1 = Teacher()
t1.say('明天就星期六了')
t1.walk(6)
t1.teacher('math')