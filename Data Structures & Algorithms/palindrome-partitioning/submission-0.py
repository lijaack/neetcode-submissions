class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            # Reached the end → the current partition is complete
            if i >= len(s):
                res.append(part.copy())
                return

            # Try every possible ending position for the next substring
            for j in range(i, len(s)):

                # Only use this substring if it is a palindrome
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])  # Choose

                    dfs(j + 1)                 # Explore

                    part.pop()                 # Undo

        dfs(0)
        return res

    def isPali(self, s, l, r):
        # Check whether s[l:r+1] reads the same forwards and backwards
        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True