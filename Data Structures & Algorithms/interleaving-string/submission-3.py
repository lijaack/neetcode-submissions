class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        
        def dfs(i,j):
            if i+j >= len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            res = False
            if i<len(s1) and s3[i+j] == s1[i]:
                res = dfs(i+1,j)
            if not res and j<len(s2)and s3[i+j] == s2[j]:
                res = dfs(i,j+1)
            memo[(i,j)] = res
            return res
             
            
        

        return dfs(0,0)