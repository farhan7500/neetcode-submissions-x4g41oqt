class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.hash_size = 1000
        self.set = []
        for _ in range(self.hash_size):
            self.set.append(ListNode(-1))

    def _get_hash(self, key):
        return key % self.hash_size

    def add(self, key):
        current = self.set[self._get_hash(key)]
        while current.next:
            if current.next.key == key:
                print(f"Key {key} already exists")
                return
            current = current.next
        current.next = ListNode(key)

    def contains(self, key):
        current = self.set[self._get_hash(key)]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False

    def remove(self, key):
        current = self.set[self._get_hash(key)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next