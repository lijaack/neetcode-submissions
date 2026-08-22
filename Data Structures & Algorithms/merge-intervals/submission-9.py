class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Find the largest starting point so we know how big to make our array
        max_val = max(interval[0] for interval in intervals)

        # mp[i] stores the END + 1 of an interval that starts at i
        # Example: [2, 5] -> mp[2] = 6
        mp = [0] * (max_val + 1)

        for start, end in intervals:
            # If multiple intervals start at the same position,
            # keep the one that extends the farthest.
            mp[start] = max(end + 1, mp[start])

        res = []

        # 'have' keeps track of the farthest point the current merged
        # interval reaches.
        have = -1

        # Start of the current merged interval
        interval_start = -1

        for i in range(len(mp)):

            # There is an interval starting at position i
            if mp[i] != 0:

                # If we aren't currently building an interval,
                # this is the start of a new merged interval.
                if interval_start == -1:
                    interval_start = i

                # Extend our current merged interval as far as necessary.
                # mp[i] is end + 1, so subtract 1 to get the actual end.
                have = max(mp[i] - 1, have)

            # We've reached the end of the current merged interval.
            # Example: have = 5 and i = 5
            if have == i:
                res.append([interval_start, have])

                # Reset so we can look for the next merged interval.
                have = -1
                interval_start = -1

        # If an interval is still open after the loop,
        # add it to the result.
        if interval_start != -1:
            res.append([interval_start, have])

        return res