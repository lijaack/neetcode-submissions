class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # Case 1: newInterval comes completely BEFORE the current interval
            # Example: newInterval = [2, 3], current = [5, 7]
            # Since there is no overlap, add newInterval and everything after it.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: newInterval comes completely AFTER the current interval
            # Example: current = [1, 3], newInterval = [5, 7]
            # No overlap, so we can safely add the current interval.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: The intervals overlap
            # Merge them into one larger interval.
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # earliest start
                    max(newInterval[1], intervals[i][1]),  # latest end
                ]

        # If we reach the end, newInterval belongs at the end.
        res.append(newInterval)
        return res