class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        res = 0
        def dfs(i,j):
            nonlocal res
        
            if (i,j) in memo:
                return memo[(i,j)]
            curr = 0
            for dr,dc in directions:
                if 0 <= i + dr < len(matrix) and 0 <= j + dc < len(matrix[0]):
                    if matrix[i+dr][j+dc] > matrix[i][j]:
                        curr = max(curr, dfs(i+dr, j+dc)) 
                        
            memo[(i,j)]= 1 + curr
            res = max(res,memo[(i,j)])

            return memo[(i,j)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)        
        return res