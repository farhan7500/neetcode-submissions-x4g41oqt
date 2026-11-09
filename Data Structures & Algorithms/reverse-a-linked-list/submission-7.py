# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # A -> B -> C -> Null
        current = head
        previous = None
        # Iterate until we hit None
        while current:
            # Save next
            tmp = current.next
            # next = previous
            current.next = previous
            # previous = current
            previous = current
            # current = next
            current = tmp

        return previous
        