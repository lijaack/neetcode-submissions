
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        components = n
        for node1, node2 in edges:      
            if dsu.union(node1,node2):
                components -=1
        return components

class DSU: 
    def __init__( self, n):
        self.parent = list(range(n))        
        self.size = [1] * n
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
        
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        #if both roots are same. they are part of the same
        if root1 == root2:
            return False
        #lets take smaller one 
        if self.size[root2] > self.size[root1]:
            root1,root2 = root2,root1
        self.parent[root2] = root1
        self.size[root1] += self.size[root2]

        return True