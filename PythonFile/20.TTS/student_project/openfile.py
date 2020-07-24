def read_from_file(filename='f.csv'):
    L = []
    try:
        f = open(filename)
        i = 0
        for line in f:
            s = line.rstrip()
            s = s.split(',')    # ['姓名','年龄','成绩']
            name, age, score = s
            if i > 0:
                print("第一次：", i)
                age = int(age)
                score = int(score)
                print(name, age, score)
                # L.append(Student(name, age, score))
                print(i)
            else:
                print(s)
            i +=1
        f.close()
    except OSError:
        print('打开文件失败！')
    return L

read_from_file(filename='si.csv')