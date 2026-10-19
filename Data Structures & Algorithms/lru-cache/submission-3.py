
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes mark the least-recent and most-recent ends
        self.left = Node()   # Least recently used
        self.right = Node()  # Most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Disconnect node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # Insert node right before the right dummy (most recent)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Accessing a key makes it the most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key and move it to most-recent position
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            # Evict the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
