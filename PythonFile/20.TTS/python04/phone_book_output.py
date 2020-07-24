
def read_info_from_file(file='phone_book.txt'):
    L = []
    try:
        f = open(file)
        while True:
            s = f.readline()
            if not s:
                break
            s = s.rstrip()
            result = s.split(',', 1)
            L.append(tuple(result))

        f.close()
    except OSError:
        print('打开文件失败！')
    return L

def print_infos(lst):
    print('+----------+--------------------+')
    print('|   name   |     number         |')
    print('+----------+--------------------+')
    for d in lst:
        t = (d[0].center(10), d[1].center(20))
        line = '|%s|%s|' % t
        print(line)
    print('+----------+--------------------+')


if __name__ == '__main__':
    L = read_info_from_file()
    print(L)
    print_infos(L)