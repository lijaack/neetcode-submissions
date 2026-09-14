class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # dp stores the answer for each state we've already calculated.
        #
        # key = (i, buying)
        # i = current day
        # buying = True  → we're allowed to buy
        # buying = False → we're holding a stock, so we can sell
        #
        # value = maximum profit we can make from this point onward
        dp = {}

        def dfs(i, buying):

            # We've gone past the last day.
            # Nothing left to buy/sell, so profit = 0.
            if i >= len(prices):
                return 0

            # If we've already solved this exact state,
            # return the answer instead of calculating it again.
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Option 1: DON'T do anything today.
            # Move to tomorrow and stay in the same state.
            cooldown = dfs(i + 1, buying)

            if buying:
                # We're allowed to buy today.
                #
                # Buy the stock:
                # - pay today's price
                # - tomorrow we're holding the stock
                buy = dfs(i + 1, not buying) - prices[i]

                # Either:
                # 1. Buy today
                # 2. Don't buy today
                dp[(i, buying)] = max(buy, cooldown)

            else:
                # We're currently holding a stock.
                #
                # Sell today:
                # - receive today's price
                # - i + 2 because tomorrow is the cooldown day
                # - after cooldown, we're allowed to buy again
                sell = dfs(i + 2, not buying) + prices[i]

                # Either:
                # 1. Sell today
                # 2. Keep holding
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        # Start on day 0.
        # We're not holding anything, so we're allowed to buy.
        return dfs(0, True)