class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for sub in res.copy():
                temp = sub.copy()
                temp.append(num)
                res.append(temp)

        return res