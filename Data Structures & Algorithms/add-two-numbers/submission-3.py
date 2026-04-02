# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode('X')
        tail = dummy

        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                sum_l1 = 0
            else:
                sum_l1 = l1.val
            if l2 is None:
                sum_l2 = 0
            else:
                sum_l2 = l2.val

            sum = sum_l1 + sum_l2 + carry
            if sum > 9:
                carry = 1
                tail.next = ListNode(sum - 10)
            else:
                carry = 0
                tail.next = ListNode(sum)
            tail = tail.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry == 1:
            tail.next = ListNode(1)

        return dummy.next
        