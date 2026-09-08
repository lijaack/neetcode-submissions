class DSU:
    def __init__(self, n):
        # Each node starts in its own group.
        self.parent = list(range(n))

        # Size of each group.
        self.size = [1] * n

    def find(self, node):
        # Follow parent pointers until we reach the root.
        while node != self.parent[node]:
            # Path compression:
            # Point node closer to the root to make future finds faster.
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return node

    def union(self, node1, node2):
        # Find the root of each node's group.
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Already in the same group, so nothing to merge.
        if root1 == root2:
            return False

        # Attach the smaller group to the larger group.
        if self.size[root2] > self.size[root1]:
            root1, root2 = root2, root1

        self.parent[root2] = root1
        self.size[root1] += self.size[root2]

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        # Initially, every node is its own component.
        components = n

        for node1, node2 in edges:
            # If they were separate groups, union() merges them.
            # Therefore, the number of components decreases by 1.
            if dsu.union(node1, node2):
                components -= 1

        return components