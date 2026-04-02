# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_orig = dummy = ListNode()
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum > 9:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            
            dummy.next = ListNode(sum)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 is None:
            while l2:
                sum = l2.val + carry
                if sum > 9:
                    carry = 1
                    sum = sum - 10
                else:
                    carry = 0
                dummy.next = ListNode(sum)
                dummy = dummy.next
                l2 = l2.next

        if l2 is None:
            while l1:
                sum = l1.val + carry
                if sum > 9:
                    carry = 1
                    sum = sum - 10
                else:
                    carry = 0
                dummy.next = ListNode(sum)
                dummy = dummy.next
                l1 = l1.next
        if carry:
            dummy.next = ListNode(carry)
        return dummy_orig.next


        