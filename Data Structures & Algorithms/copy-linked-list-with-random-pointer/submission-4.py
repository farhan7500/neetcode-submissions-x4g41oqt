"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
                return None

        # Step 1: Create a mapping of Old Node -> New Node
        # We don't worry about the pointers yet, just create the copies.
        old_to_new = {}
        
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Wire up the next and random pointers
        current = head
        while current:
            # Get the new copy we made for the current old node
            new_node = old_to_new[current]
            
            # Point the new node's next to the copy of the old node's next
            new_node.next = old_to_new.get(current.next)
            
            # Point the new node's random to the copy of the old node's random
            new_node.random = old_to_new.get(current.random)
            
            current = current.next

        return old_to_new[head]

        