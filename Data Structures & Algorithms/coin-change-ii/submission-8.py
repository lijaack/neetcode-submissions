class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, a):
            # We made the amount exactly
            if a == 0:
                return 1

            # No more coin options to add
            if i >= len(coins):
                return 0

            if (i, a) in memo:
                return memo[(i, a)]
            res = dfs(i + 1, a)
            # Don't add this coin yet
            # Add this coin and stay here so we can use it again
            if a >= coins[i]:
                
                res += dfs(i, a - coins[i])

            memo[(i, a)] = res
            return res

        return dfs(0, amount)