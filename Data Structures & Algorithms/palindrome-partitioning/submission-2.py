class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [],[]

        def dfs (i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                
                if isPali(i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        def isPali(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1

            return True
        dfs(0)
        return res
        