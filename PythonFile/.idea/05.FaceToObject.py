#面向对象编程

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' %(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            print('A')
            return 'A'
        elif self.score >= 60:
            print('B')
            return 'B'
        else:
            print('C')
            return 'C'

    #获取类的属性name和score
    def get_name(self):
        print(self._name)
        return self._name

    def get_score(self):
        print(self._score)
        return self._score
    #修改类的属性name和score
    def set_score(self, score):
        if 0 <= score <=100:
            self.score = score
        else:
            raise ValueError('bad score!')

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simple', 87)
bart.print_score()
lisa.print_score()
lisa.get_grade()