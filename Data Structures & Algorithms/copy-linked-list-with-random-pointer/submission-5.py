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
        mapping = {}

        current = head
        # Map current and new node
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        current = head
        # Wire next and random
        while current:
            new_node = mapping[current]
            new_node.next = mapping.get(current.next)
            new_node.random = mapping.get(current.random)

            current = current.next

        return mapping[head]

        