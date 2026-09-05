class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def dfs(r,c,a):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0
            ):
                return a   
            grid[r][c] = 0
            for dr, dc in directions:
                    a = dfs(r+dr, c+dc, a)

            return (1+a)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c,0))


        return res
