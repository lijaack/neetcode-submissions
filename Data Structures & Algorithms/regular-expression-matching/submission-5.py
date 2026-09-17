class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            # Both strings completely matched
            if i == len(s) and j == len(p):
                return True

            # Pattern is finished but s still has characters
            if j == len(p):
                return False

            # s is finished: remaining pattern must be able to make ""
            if i == len(s):
                if j + 1 < len(p) and p[j + 1] == "*":
                    return dfs(i, j + 2)
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            curr = False

            # Current characters match
            if s[i] == p[j] or p[j] == ".":
                curr = dfs(i + 1, j + 1)

            # Next pattern character is *
            if j + 1 < len(p) and p[j + 1] == "*":
                # Option 1: use * to match another s[i]
                if s[i] == p[j] or p[j] == ".":
                    curr = curr or dfs(i + 1, j)

                # Option 2: use * zero times
                curr = curr or dfs(i, j + 2)

            dp[(i, j)] = curr
            return curr

        return dfs(0, 0)