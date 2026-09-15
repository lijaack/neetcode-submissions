class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            if buying:
                buy_price = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1,buying)
                dp[(i,buying)] = max(buy_price,cooldown)
            else:
                sell_price = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1,buying)
                dp[(i,buying)] = max(sell_price,cooldown)
            return dp[(i,buying)]
        
        return dfs(0,1)