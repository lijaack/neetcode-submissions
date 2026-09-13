class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp[i][j] = length of the longest common subsequence
        # between text1[i:] and text2[j:].
        #
        # Extra row and column represent reaching the end of either string.
        # If one string is empty, the LCS length is 0.
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        # Work backwards because dp[i][j] depends on:
        #   dp[i + 1][j + 1]  -> both characters match
        #   dp[i + 1][j]      -> skip text1[i]
        #   dp[i][j + 1]      -> skip text2[j]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                # If the current characters match,
                # include this character in the LCS.
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # If they don't match, we have two choices:
                # skip text1[i] OR skip text2[j].
                # Take whichever gives the longer subsequence.
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # dp[0][0] represents the LCS of the two entire strings.
        return dp[0][0]