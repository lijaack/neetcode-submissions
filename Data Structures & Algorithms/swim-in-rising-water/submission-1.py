class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        min_heap=[[grid[0][0],0,0]]
        visited = set()
        visited.add((0,0))
        while min_heap:
            t,r,c = heapq.heappop(min_heap)
            if r == n-1 and c == n-1:
                return t
            for dr,dc in directions:
                neiR, neiC = r+dr, c+dc
                if min(neiR,neiC) < 0 or max(neiR,neiC) >= n or (neiR,neiC) in visited:
                    continue
                heapq.heappush(min_heap, [max(t,grid[neiR][neiC]), neiR,neiC])
                visited.add((neiR,neiC))
