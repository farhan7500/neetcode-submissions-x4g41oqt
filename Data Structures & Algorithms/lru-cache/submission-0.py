class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertToEnd(self, node):
        prev_node = self.tail.prev
        node.prev = prev_node
        prev_node.next = node
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertToEnd(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.head.next.key]
            self.removeNode(self.head.next)
        self.insertToEnd(node)
