class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        # One way to decode an empty string
        dp[n] = 1

        for i in range(n - 1, -1, -1):

            # Can't decode a single 0
            if s[i] != "0":
                # Take one digit
                dp[i] = dp[i + 1]

            # Try taking two digits
            if i + 1 < n:
                two_digits = int(s[i:i + 2])

                if 10 <= two_digits <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]