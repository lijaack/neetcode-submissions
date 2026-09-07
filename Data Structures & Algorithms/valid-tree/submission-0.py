class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges.
        # More than n - 1 means there must be a cycle.
        if len(edges) > n - 1:
            return False

        # Build an undirected adjacency list.
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()

        def dfs(node, parent):
            # Reaching a visited node through a different path means
            # we found a cycle.
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj[node]:
                # Ignore the edge we used to get to this node.
                if neighbor == parent:
                    continue

                # If the neighbor leads to a cycle, the whole graph is invalid.
                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS at node 0. It has no real parent, so use -1.
        # Then make sure DFS reached every node (the graph is connected).
        return dfs(0, -1) and len(visited) == n