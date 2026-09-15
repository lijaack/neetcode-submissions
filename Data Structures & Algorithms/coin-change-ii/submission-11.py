class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i,a):
            if a == 0:
                return 1
            if i >=len(coins):
                return 0
            if (i,a) in memo:
                return memo[(i,a)]
            #skip this coin
            res = dfs(i+1, a)
            #use this coin
            if a >= coins[i]:
                res += dfs(i, a-coins[i])
            memo[(i,a)] = res
            return res
            
        return dfs(0,amount)
                         

