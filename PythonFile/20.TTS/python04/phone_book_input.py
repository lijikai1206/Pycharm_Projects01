def input_phone_number():
    '''此函数用来读取用户输入，形成元组列表并返回'''
    L = []
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        number = input("请输入电话：")
        L.append((name, number))
    return L

def write_to_file(lst, filenaem='phone_book.txt'):
    try:
        f = open(filenaem, 'a+')
        for name, number in lst:
            f.write(name)
            f.write(',')
            f.write(number)
            f.write('\n')
        f.close()
    except OSError:
        print('打开文件失败！')

if __name__ == '__main__':
    L = input_phone_number()
    print(L)
    write_to_file(L)