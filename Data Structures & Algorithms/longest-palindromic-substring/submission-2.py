class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0,0
        #count it
        n= len(s)
        #make the 2d grid
        dp = [[False]*n for _ in range(n)]
        #outer loop going backwards
        for i in range(n-1, -1, -1):
            #inner loop, starting for i
            for j in range(i,n):
                #check if i = j, AND j-i <=2 OR i+1 and j-1 is true
                if s[i] == s[j] and (j-i <=2 or dp[i+1][j-1]):
                    #SET DP I,J TRUE
                    dp[i][j] = True
                    #THEN CHECK CURR RESLEN > SAVED RESLEN
                    if j-i+1 > resLen:
                        resIdx = i
                        resLen = j-i+1
                        #if yes, set residx to i
                        #set reslen to j-i
        
        return s[resIdx:resIdx+resLen]
