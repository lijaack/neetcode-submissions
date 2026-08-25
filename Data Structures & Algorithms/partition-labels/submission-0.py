class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        #marks last index for each letter
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            #compare new letters last index. if the last index is further down then it becomes the new goal
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res