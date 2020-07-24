import collections
#创建双向队列
d1 = collections.deque()
d1.append(1)
d1.appendleft('left')

print(d1)