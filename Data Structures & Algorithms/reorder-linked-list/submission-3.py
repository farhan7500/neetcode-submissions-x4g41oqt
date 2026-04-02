# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        previous = None
        while slow is not None:
            next = slow.next
            slow.next = previous

            previous = slow
            slow = next

        current = head

        count = 0
        dummy = ListNode('X')
        tail = dummy
        while previous is not None and current is not None:
            if count % 2 == 0:
                tail.next = current
                current = current.next
            else:
                tail.next = previous
                previous = previous.next
            tail = tail.next
            count += 1
        head = dummy.next
        