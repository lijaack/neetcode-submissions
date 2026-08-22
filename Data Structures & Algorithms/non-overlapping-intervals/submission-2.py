class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Sort by START time.
        # Example:
        # [[1,3], [2,4], [3,5]]
        # stays [[1,3], [2,4], [3,5]]
        intervals.sort()

        # Number of intervals we need to remove
        res = 0

        # End time of the interval we're currently keeping
        prevEnd = intervals[0][1]

        # Check every interval after the first one
        for start, end in intervals[1:]:

            # No overlap.
            # Example:
            # prev interval = [1,3]
            # current        = [3,5]
            # start (3) >= prevEnd (3)
            #
            # We can keep the current interval.
            if start >= prevEnd:
                prevEnd = end

            else:
                # OVERLAP!
                # Example:
                # prev interval = [1,5]
                # current        = [2,3]
                #
                # We have to remove one of them.
                res += 1

                # GREEDY CHOICE:
                # Keep whichever interval ends earlier.
                #
                # [1,5] -> ends at 5
                # [2,3] -> ends at 3
                #
                # Keep [2,3] because ending earlier leaves
                # more room for future intervals.
                prevEnd = min(end, prevEnd)

        return res