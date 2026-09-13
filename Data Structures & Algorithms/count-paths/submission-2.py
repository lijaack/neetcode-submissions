class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Create an (m+1) x (n+1) DP grid.
        # The extra row/column lets us safely access dp[i+1][j]
        # and dp[i][j+1] without going out of bounds.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Starting from the bottom-right destination.
        # There is exactly 1 way to be at the destination:
        # you're already there.
        dp[m - 1][n - 1] = 1

        # Work backwards from the bottom row toward the top.
        for i in range(m - 1, -1, -1):

            # Work backwards from the right column toward the left.
            for j in range(n - 1, -1, -1):

                # Number of paths from (i,j) =
                # paths going DOWN + paths going RIGHT.
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        # dp[0][0] contains the number of ways
        # to travel from the top-left to the bottom-right.
        return dp[0][0]