# 1.用泪来描述一个学生的信息（可以修改之前写的student类）
#   class Student:
#           # 此处实现
#   要求该类的对象用于存储学生信息：姓名，年龄，成绩
#   将这些对象存于列表中，可以任意添加和删除学生信息
#       1.打印学生的个数
#       2.打印出所有学生的平均成绩
#   （建议用类变量存储学生的个数，也可以把列表当作类变量）

class Student:
    count = 0    # 此类变量用来记录学生的个数
    # docs = []    # 此列表保存所有的学生对象
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s
        Student.count += 1      # 让对象个数加1

    def __del__(self):
        Student.count -= 1      # 对象销毁时count减1

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score

    def get_infos(self):
        return (self.name, self.age, self.score)

    def set_score(self, score):
        '''此方法用于定制设置成绩的规则'''
        if 0 <= score <= 100:
            self.score = score
            return
        raise ValueError('不合法的成绩信息：' + str(score))

    def is_name(self, n):
        '''判断n是否和self的名字相同'''
        return self.name == n

    def write_to_file(self, file):
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')

    @classmethod
    def getTotalCount(cls):
        # 此方法用来得到学生对象的个数
        return cls.count


def test():
    L = []          # 1班的学生
    L.append(Student('小张', 20, 100))
    L.append(Student('小王', 18, 97))
    L.append(Student('小张', 19, 98))
    print("此时学生对象的个数是：", Student.getTotalCount())

    L2 = []         # 2班的学生
    L2.append(Student('小赵', 19,89))
    print("L2列表中的个数是：", Student.getTotalCount())
    # 删除L中的一个学生
    L.pop(1)
    print("此时学生个数为：", Student.getTotalCount())

    all_student = L + L2
    scores = 0
    for s in all_student:
        # scores += s.score
        scores += s.get_score()

    print("平均成绩是：", scores/len(all_student))


if __name__ == '__main__':
    test()