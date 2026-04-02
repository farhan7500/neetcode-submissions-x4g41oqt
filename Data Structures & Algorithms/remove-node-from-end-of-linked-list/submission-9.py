# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trailer = dummy = ListNode(0, head)
        leader = head
        for _ in range(n):
            leader = leader.next
        while leader:
            leader = leader.next
            trailer = trailer.next
        trailer.next = trailer.next.next

        return dummy.next
        

        