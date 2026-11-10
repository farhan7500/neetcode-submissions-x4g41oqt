# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # Find mid point
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse_ll(node):
            current = node
            previous = None
            while current:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp
            return previous

        # Set up first and second
        first = head
        second = reverse_ll(slow.next)

        slow.next = None

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        