class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        res = 0
        currMax = 0
        currMin = 0

        for num in nums:
            cMax = currMax*num
            cMin = currMin*num
            currMax = max(num, cMax, cMin)
            currMin = min(num, cMax, cMin)
            res = max(res,currMax)
        return res