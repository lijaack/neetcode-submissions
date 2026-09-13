class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        # Cheapest price to reach each city.
        # Initially, only the source city is reachable.
        prices = [float("inf")] * n
        prices[src] = 0

        # k stops means we can take at most k + 1 flights.
        for _ in range(k + 1):

            # Represents prices after taking ONE more flight.
            # We copy so we don't use an update from this same
            # round to take multiple flights in one iteration.
            tmp_prices = prices.copy()

            # Try every flight as a possible next flight.
            for source, destination, price in flights:

                # If we can't currently reach the source,
                # this flight cannot be used yet.
                if prices[source] == float("inf"):
                    continue

                # Try reaching destination through this flight.
                new_price = prices[source] + price

                # Keep the cheaper way to reach destination.
                if new_price < tmp_prices[destination]:
                    tmp_prices[destination] = new_price

            # Move to the results from this round.
            prices = tmp_prices

        # If destination is still unreachable, return -1.
        if prices[dst] == float("inf"):
            return -1

        return prices[dst]