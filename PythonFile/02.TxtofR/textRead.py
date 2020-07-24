import os

txt = open("xlwt使用方法.txt","r").read()
print(txt)


def zhengze(f):
    new_lines = []
    regex_str = ".*?Demo_.*(\d*).*"
    for x in f:
        new_x = x.splitlines()  # 注意：splitlines是将传入的字符串去除'\n'之后以数组的形式传出，而不是字符串形式
        match_obj = re.match(regex_str, new_x[0])
        if match_obj:
            new_lines.append(match_obj.group(1))
        else:
            new_lines.append('no')
    return new_lines
    print()