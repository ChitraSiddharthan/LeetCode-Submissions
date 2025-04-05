# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy

        cForward = 0
        while l1 or l2 or cForward:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            newVal = v1 + v2 + cForward
            cForward = newVal // 10
            newVal = newVal % 10
            current.next = ListNode(newVal)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

