w =int(input("请输入宽度："))
for y in range(1, w+1):
    for x in range(y, y+w):
        print("%2d" % x, end='')
    print()  #换行