class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # If t is longer than s, we cannot possibly form t from s
        if len(t) > len(s):
            return 0

        # dp[(i, j)] = number of ways to form t[j:]
        # using characters from s[i:]
        dp = {}

        def dfs(i, j):

            # We successfully matched all of t
            # There is 1 valid way to complete it
            if j == len(t):
                return 1

            # We ran out of s before finishing t
            # Therefore, there are 0 ways
            if i == len(s):
                return 0

            # We already calculated this state
            # Return the saved answer instead of recalculating
            if (i, j) in dp:
                return dp[(i, j)]

            # Option 1:
            # Skip s[i] and continue looking for t[j]
            res = dfs(i + 1, j)

            # Option 2:
            # If s[i] matches t[j], we can use s[i]
            # to match t[j], so move forward in both strings
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            # Save the total number of ways for this state
            dp[(i, j)] = res

            return res

        # Start at the beginning of both strings
        return dfs(0, 0)