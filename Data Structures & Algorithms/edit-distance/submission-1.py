class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i,j):
            if i == len(word1) and j == len(word2) :
                return 0
            if i < len(word1) and j == len(word2):
                return len(word1)-i
            if i == len(word1) and j < len(word2):
                return len(word2)-j

            if (i,j) in dp:
                return dp[(i,j)]
            curr = 0
            #case 1 same letter we i and j + 1
            if word1[i] == word2[j]:
               curr =  dfs(i+1,j+1)
            #case 2 we check 1 letter ahead. if its the same, we can skip or change and return min
            else: 
              curr = 1 + min(dfs(i+1,j), dfs(i+1,j+1), dfs(i,j+1))
            dp[(i,j)] = curr

            return dp[(i,j)]

        return dfs(0,0)


