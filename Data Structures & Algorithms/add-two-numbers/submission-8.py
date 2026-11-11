# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        current = dummy
        value1 = 0
        value2 = 0
        while l1 or l2 or carry:
            if l1:
                value1 = l1.val
            else:
                value1 = 0
            if l2:
                value2 = l2.val
            else:
                value2 = 0

            addition = value1 + value2 + carry
            if addition > 9:
                carry = 1
                current.next = ListNode(addition - 10)
            else:
                carry = 0
                current.next = ListNode(addition)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next
        return dummy.next
