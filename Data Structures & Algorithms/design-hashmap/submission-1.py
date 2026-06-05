class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hash_size = 1000
        self.set = []
        for _ in range(self.hash_size):
            self.set.append(ListNode(-1, -1))

    def _get_hash(self, key):
        return key % self.hash_size

    def put(self, key, val):
        current = self.set[self._get_hash(key)]
        while current.next:
            if current.next.key == key:
                current.next.val = val
                return
            current = current.next
        current.next = ListNode(key, val)

    def get(self, key):
        current = self.set[self._get_hash(key)]
        while current.next:
            if current.next.key == key:
                return current.next.val
            current = current.next
        return -1

    def remove(self, key):
        current = self.set[self._get_hash(key)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)