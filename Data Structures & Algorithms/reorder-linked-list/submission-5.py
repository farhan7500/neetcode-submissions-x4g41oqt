# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        # At this point, slow is at the middle
        # Reverse the second half
        first = head
        second = self.reverse_list(slow.next)

        slow.next = None

        # Set the nodes in desired order
        # A -> B -> C -> D
        # X -> y -> Z


        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

    @staticmethod
    def reverse_list(node):
        previous = None
        current = node

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

        