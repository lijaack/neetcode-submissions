class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount < 0:
                return float("inf")

            if amount in memo:
                return memo[amount]

            best = float("inf")

            for coin in coins:
                best = min(best, 1 + dfs(amount - coin))

            memo[amount] = best
            return best

        result = dfs(amount)

        if result == float("inf"):
            return -1

        return result