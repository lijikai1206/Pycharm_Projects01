# 读取文本中的中英文数据并使用正则表达式将所需数据筛选入到一个新文本中
import re
import os

# zhengze函数对读取到的数据进行筛选，并将筛选好的数据存入数组new_lines
new_lines = []  # 申明new_lines数组


def zhengze(f):
    regex_str = ".*?(l.*?e).*"
    for x in f:
        new_x = x.splitlines()  # 注意：splitlines是将传入的字符串去除'\n'之后以数组的形式传出，而不是字符串形式
        match_obj = re.match(regex_str, new_x[0])
        if match_obj:
            new_lines.append(match_obj.group(1))
        else:
            new_lines.append('no')
    return new_lines


# 获取指定文件夹下的所有文本的绝对地址，并存入数组file_path
path = "C:\Users\lijik\PycharmProjects\001.files\02.TxtofR\xlwt使用方法.txt"
file_path = []
for filename in os.listdir(path):  # 获取path下所有文件的路径
    file_path.append((os.path.join(path, filename)))
print
file_path

# 对每个文本调用正则函数进行筛选,筛选过后的数据存入数组final
for adress in file_path:
    file_object = open(adress)
    lines = file_object.readlines()  # 将文本中的内容以数组的形式（每行为一个元素）赋给lines
    file_object.close()
    final = zhengze(lines)
print
final

# 将筛选出来的数据写入新文本re_new.txt
file_2 = open("re_new.txt", 'w+')
for x in final:
    file_2.write(x)
    file_2.write('\n')
file_2.close()