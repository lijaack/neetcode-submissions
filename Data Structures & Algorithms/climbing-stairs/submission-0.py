class Solution:
    def climbStairs(self, n: int) -> int:

        # If there are only 1 or 2 stairs,
        # there are exactly n ways to reach the top.
        # n = 1 → [1]
        # n = 2 → [1+1], [2]
        if n <= 2:
            return n

        # dp[i] = number of different ways to reach stair i.
        # We create n + 1 spots so we can use the stair number
        # directly as the index.
        dp = [0] * (n + 1)

        # Base cases:
        # 1 stair → 1 way
        # 2 stairs → 2 ways
        dp[1], dp[2] = 1, 2

        # To reach stair i, the last step must have come from:
        # i - 1 (take 1 step)
        # OR
        # i - 2 (take 2 steps)
        #
        # So we add the number of ways to reach those two stairs.
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # dp[n] contains the total number of ways to reach the top.
        return dp[n]