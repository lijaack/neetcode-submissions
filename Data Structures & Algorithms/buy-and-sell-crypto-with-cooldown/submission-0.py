class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][buying]:
        # maximum profit we can make starting at day i
        #
        # buying = 1 → we are allowed to buy
        # buying = 0 → we are holding a stock, so we can sell
        #
        # Extra row lets us safely reference dp[n].
        dp = [[0] * 2 for _ in range(n + 1)]

        # Work backwards because today's answer depends
        # on future days.
        for i in range(n - 1, -1, -1):

            # Try both states:
            # buying = True  → deciding whether to buy
            # buying = False → deciding whether to sell
            for buying in [True, False]:

                if buying:

                    # Option 1: BUY today.
                    # Spend prices[i], then tomorrow we're holding,
                    # so buying becomes False.
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]

                    # Option 2: DON'T buy today.
                    # Stay in the buying state and move to tomorrow.
                    cooldown = dp[i + 1][True] if i + 1 < n else 0

                    # Take whichever gives more profit.
                    dp[i][1] = max(buy, cooldown)

                else:

                    # Option 1: SELL today.
                    # Receive prices[i].
                    #
                    # After selling, tomorrow is a cooldown day,
                    # so we jump to i + 2 and become allowed to buy again.
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]

                    # Option 2: DON'T sell today.
                    # Keep holding and move to tomorrow.
                    cooldown = dp[i + 1][False] if i + 1 < n else 0

                    # Take whichever gives more profit.
                    dp[i][0] = max(sell, cooldown)

        # Start on day 0 with permission to buy.
        return dp[0][1]