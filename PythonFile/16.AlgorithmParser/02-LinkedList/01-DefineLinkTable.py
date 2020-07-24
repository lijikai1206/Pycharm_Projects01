
class Node(object):
    '''定义单链表节点类'''
    def __init__(self,data,next = None):
        '''data为数据项，next为下一节点的链接，初始化节点默认链接为None'''
        self.data = data
        self.next = next

# 定义3个节点对象分别为node1、node2和node3
node1 = None
node2 = Node(1, None)
node3 = Node('hello', node2)
print(node1)
print(node2.data, node2)
print(node3.data, node3.next, node3.next.next)