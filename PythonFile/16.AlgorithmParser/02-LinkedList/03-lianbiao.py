# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import ListNode
class Solution:
    def reversePrint(self, head: ListNode):
        newlist = []
        while head:
            newlist.append(head.val)
            head = head.next
        return newlist[::-1]

head = [1, 3, 2, 4]
r = Solution().reversePrint(head)
print(r)