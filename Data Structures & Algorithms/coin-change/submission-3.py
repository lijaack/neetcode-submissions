class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[a] = fewest coins needed to make amount "a"
        #
        # Start every amount at an impossible number.
        # amount + 1 is guaranteed to be bigger than any possible
        # valid answer (if a 1-coin exists, the worst case is "amount" coins).
        dp = [amount + 1] * (amount + 1)

        # Base case:
        # It takes 0 coins to make amount 0.
        dp[0] = 0

        # Build the answers from small amounts → bigger amounts.
        for a in range(1, amount + 1):

            # Try every coin as the LAST coin we use.
            for c in coins:

                # We can only use this coin if it doesn't make
                # the amount negative.
                if a - c >= 0:

                    # If we use coin c:
                    #   dp[a - c] = fewest coins needed for the remaining amount
                    #   + 1       = the coin we're using right now
                    #
                    # Take the minimum over all possible coins.
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] is still amount + 1, we never found a way
        # to make the target, so return -1.
        return dp[amount] if dp[amount] != amount + 1 else -1