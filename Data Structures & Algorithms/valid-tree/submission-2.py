class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        neighbors = [[] for _ in range(n)] 

        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in neighbors[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
                     
            return True

        return dfs(0,-1) and len(visited) == n