class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # If there are no existing intervals, the new interval is the answer
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]

        # Binary search for where the new interval should be inserted.
        # We compare starting points of the intervals.
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < target:
                # newInterval starts after this interval,
                # so search to the right
                left = mid + 1
            else:
                # newInterval starts before or at this interval,
                # so search to the left
                right = mid - 1

        # Insert newInterval in its sorted position
        intervals.insert(left, newInterval)

        res = []

        # Now merge any overlapping intervals
        for interval in intervals:

            # No overlap:
            # either res is empty, or the current interval
            # starts after the previous interval ends
            if not res or res[-1][1] < interval[0]:
                res.append(interval)

            else:
                # Overlap → extend the previous interval's end
                # to whichever interval ends later
                res[-1][1] = max(res[-1][1], interval[1])

        return res