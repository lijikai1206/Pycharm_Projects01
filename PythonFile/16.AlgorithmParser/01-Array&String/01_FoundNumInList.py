li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def search(someone, li):
    l = -1
    h = len(li)

    while l + 1 != h:
        m = int((l + h) / 2)
        if li[m] < someone:
            l = m
        else:
            h = m
    p = h
    if p >= len(li) or li[p] != someone:
        print("元素不存在")
    else:
        str = "元素索引为%d" % p
        print(str)


search(3, li)  # 元素索引为2