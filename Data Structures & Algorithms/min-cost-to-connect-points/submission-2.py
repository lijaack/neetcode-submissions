class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        node=0
        dist = [float("inf") ]* n
        visited = set()
        edges = 0
        total_distance = 0
        while edges < n-1:
            visited.add(node)
            next_node=-1
            for i in range(n):
                if i in visited:
                    continue
                                    
                curr_distance = (
                    abs(points[i][0] - points[node][0]) +
                    abs(points[i][1] - points[node][1])
                )
                dist[i] = min(dist[i], curr_distance)
                if next_node == -1 or dist[i]<dist[next_node]:
                    next_node = i
            node = next_node
            total_distance += dist[node]
            edges+=1 
        return total_distance