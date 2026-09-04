class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1], [-1, 0], [0,-1]]
        r,c = len(grid), len(grid[0])
        islands = 0
        
        # def dfs(i,j):
        #     grid[i][j] = "0"
        #     for dr,dc in directions:
        #         if grid[i+dr][j+dc] and grid[i+dr][j+dc] == "1":
        #             dfs(i+dr, j+dc)
        #     return
        def dfs(i, j):
            grid[i][j] = "0"

            for dr, dc in directions:
                ni, nj = i + dr, j + dc

                if (ni >= 0 and ni < r and
                    nj >= 0 and nj < c and
                    grid[ni][nj] == "1"):
                    dfs(ni, nj)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1
        return islands