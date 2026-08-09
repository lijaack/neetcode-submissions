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

        # Step 1: Insert a copy of each node directly after the original.
        current = head

        while current is not None:
            copy = Node(current.val)

            copy.next = current.next
            current.next = copy

            current = copy.next

        # The first copied node is the second node.
        new_head = head.next

        # Step 2: Set the random pointers of the copied nodes.
        current = head

        while current is not None:
            if current.random is not None:
                current.next.random = current.random.next

            current = current.next.next

        # Step 3: Separate the original list from the copied list.
        current = head

        while current is not None:
            copy = current.next

            current.next = copy.next

            if copy.next is not None:
                copy.next = copy.next.next

            current = current.next

        return new_head
