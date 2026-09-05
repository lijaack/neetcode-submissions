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
        if head is None:
            return None

        oldToCopy = {}

        # Create a copy of every node
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        # Connect next and random pointers
        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy.get(cur.next)
            oldToCopy[cur].random = oldToCopy.get(cur.random)
            cur = cur.next

        return oldToCopy[head]