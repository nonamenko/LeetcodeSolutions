# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        res = current = ListNode()
        prev = 0
        while (l1 or l2):
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            v = v1 + v2 + prev
            prev = v // 10
            v %= 10
            current.val = v
            next_node = ListNode()
            current.next = next_node
            prevNode = current
            current = next_node
        if prev:
            current.val = prev
        else:
            prevNode.next = None
        return res
        