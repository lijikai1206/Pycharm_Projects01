# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#         使用追逐法(双指针),fast每次走两步,slow每次走一步
        if head==None or head.next==None:
            return False
        fast=head.next
        slow=head
        while fast!=None:
            if fast==slow:
                return True
            fast=fast.next
            if fast==None:
                return False
            fast=fast.next
            slow=slow.next
        return False


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 深度拷贝
class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        result = self.dfs(head)
        return result

    def dfs(self, head):
        if not head: return None
        if head in self.visited:
            return self.visited[head]
        # 创建新结点
        copy = Node(head.val, None, None)
        self.visited[head] = copy
        copy.next = self.dfs(head.next)
        copy.random = self.dfs(head.random)
        return copy
