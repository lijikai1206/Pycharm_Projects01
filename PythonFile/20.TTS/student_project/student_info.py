# 4.修改之前的学生信息管理程序，实现添加菜单和选择菜单操作功能
#   菜单：
#       1)添加学生信息
#       2)查看所有学生信息
#       3）修改学生信息
#       4）删除学生信息
#       5）按成绩从高至低打印学生信息
#       6）按成绩从低至高打印学生信息
#       7）按年龄从大到小打印学生信息
#       8）按年龄从小到大打印学生信息 （要求原来输入的列表顺序保持不变）
#       q）退出
#   请选择：1
#          请输入姓名：。。。。
#   请选择：3
#       请输入修改学生的姓名：。。。。
#   (要求每个功能都对应一个函数）
from student import Student

def input_student():
    # 此函数获取学生信息，并返回信息的字典的方法
    L = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = input("请输入学生年龄：")
        score = input("请输入学生成绩：")
        d = Student(name, age, score)
        # d = {}
        # d['name'] = name
        # d['age'] = age
        # d['score'] = score
        L.append(d)
    return L

def output_student(L):
    # 以表格形式在大英学生信息
    print('+------------+------+-------+')
    print('|    name    |  age | score |')
    print('+------------+------+-------+')
    for d in L:
        n, a, s = d.get_infos()
        t = (n.center(12),
        str(a).center(6),
        str(s).center(7))        # t是元组
        line = "|%s|%s|%s|" % t
        print(line)
    print('+------------+------+-------+')

# 此函数用来改写学生信息
def modify_student_info(lst):
    name = input("请输入要修改的学生的姓名：")
    for d in lst:
        # if d['name'] == name:
        if d.is_name(name):
            score = int(input("请输入新的成绩："))
            d.set_score = score
            # d['score'] = score
            print("修改", name, '的成绩为', score)
            return
    else:
        print("没有找到名为：", name, "的学生信息！")
    return lst

# 删除学生信息的函数
def delete_student_info(lst):
    name = input("请输入要删除学生的姓名：")
    for i in range(len(lst)):
        if lst[i].is_name(name):
            del lst[i]
            print("已成功删除：", name)
            return True
    else:
        print("没有找到名为：", name, "的学生")

#       5）按成绩从高至低打印学生信息
def print_by_score_desc(lst):
    L = sorted(lst, key=lambda d: d.get_score(), reverse=True)
    print(L)
    output_student(L)

#       6）按成绩从低至高打印学生信息
def print_by_score_asc(lst):
    L = sorted(lst, key=lambda d: d.get_score())
    print(L)
    output_student(L)

#       7）按年龄从大到小打印学生信息
def print_by_age_desc(lst):
    L = sorted(lst, key=lambda d: d.get_age(), reverse=True)
    print(L)
    output_student(L)

#       8）按年龄从小到大打印学生信息
def print_by_age_asc(lst):
    L = sorted(lst, key=lambda d: d.get_age())
    print(L)
    output_student(L)

def save_to_file(docs, filename='si.csv'):
    try:
        f = open(filename, 'a+')
        print(f.readline())
        # if "" == f.readline():
        #     f.write("name, age, score" + "\n")
        # else:
        for stu in docs:
            stu.write_to_file(f)
        f.close()
        print('保存文件成功！')
    except OSError:
        print('保持失败！')

def read_from_file(filename='si.csv'):
    L = []
    try:
        f = open(filename)
        for line in f:
            s = line.rstrip()
            s = s.split(',')    # ['姓名','年龄','成绩']
            print(s)
            name, age, score = s
            age = int(age)
            score = int(score)
            print(name, age, score)
            L.append(Student(name, age, score))
        f.close()
    except OSError:
        print('打开文件失败！')
    return L



# L = input_student()
# output_student(L)
# read_from_file(filename='si.txt')
# save_to_file(L, filename='si.csv')


