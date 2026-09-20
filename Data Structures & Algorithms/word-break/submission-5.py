class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = {}

        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            memo[i] = False
            for j in range(i,len(s)):
                if s[i:j+1] in wordset and not memo[i]:
                    memo[i] = dfs(j+1)
            return memo[i]
        

        return dfs(0)