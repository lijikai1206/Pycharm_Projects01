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