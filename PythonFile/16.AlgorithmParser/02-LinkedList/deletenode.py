
class ListNode(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

class CreateLinkTable():
    def __init__(self, list):
        head =None
        for lst in list:
            ListNode(lst, head)
        self.head = head


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head


head = [1, 5, 6, 8, 10]
val = 6
r = CreateLinkTable(head)
# r = Solution().deleteNode(head, val)
print(r)
