class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Each node starts as its own group.
        parent = [i for i in range(len(edges) + 1)]

        # Size of each group.
        size = [1] * (len(edges) + 1)

        def find(node):
            # Follow parent pointers until we reach the root.
            while node != parent[node]:
                # Path compression: make the path shorter for next time.
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node

        def union(node1, node2):
            # Find the root of each node's group.
            root1 = find(node1)
            root2 = find(node2)

            # Already in the same group → this edge creates a cycle.
            if root1 == root2:
                return False

            # Attach the smaller group to the larger group.
            if size[root2] > size[root1]:
                root1, root2 = root2, root1

            parent[root2] = root1
            size[root1] += size[root2]

            return True

        # Process each edge.
        for node1, node2 in edges:
            # If union fails, these nodes were already connected.
            if not union(node1, node2):
                return [node1, node2]
