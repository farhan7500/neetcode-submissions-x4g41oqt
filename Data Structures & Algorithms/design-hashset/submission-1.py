class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = []
        for _ in range(10000):
            self.set.append(ListNode(0))

    def _get_hash(self, key):
        return key % 10000

    def add(self, key: int) -> None:
        current = self.set[self._get_hash(key)]

        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next  = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.set[self._get_hash(key)]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.set[self._get_hash(key)]

        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False