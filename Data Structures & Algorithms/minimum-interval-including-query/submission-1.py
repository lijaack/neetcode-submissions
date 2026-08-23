class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # Sort intervals by their LEFT endpoint.
        # This lets us move through the intervals only once
        # as the queries get larger.
        intervals.sort()

        # Min-heap stores:
        # (interval length, right endpoint)
        #
        # The heap is ordered by interval length,
        # so minHeap[0] is always the shortest interval.
        minHeap = []

        # Dictionary to store:
        # query -> answer
        #
        # We process queries in sorted order for efficiency,
        # but need to return answers in the original query order.
        res = {}

        # Pointer to the next interval we haven't added yet.
        i = 0

        # Process queries from smallest → largest.
        for q in sorted(queries):

            # Add every interval that has STARTED by this query.
            #
            # Because intervals are sorted by left endpoint,
            # i only moves forward and never needs to go backward.
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]

                # Store:
                #   interval length = r - l + 1
                #   right endpoint  = r
                #
                # Heap prioritizes the shortest interval.
                heapq.heappush(minHeap, (r - l + 1, r))

                i += 1

            # Remove intervals that have already ENDED
            # before the current query.
            #
            # If r < q, then q is outside the interval.
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # If there are valid intervals remaining,
            # the heap's first element is the shortest one.
            #
            # Otherwise, no interval contains q → -1.
            res[q] = minHeap[0][0] if minHeap else -1

        # We processed queries in sorted order,
        # so rebuild the answers in the ORIGINAL query order.
        return [res[q] for q in queries]