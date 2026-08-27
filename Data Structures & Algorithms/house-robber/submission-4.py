class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        if len(nums)<3:
            return max(nums[0],nums[1])
        n = len(nums)
        res = 0
        nums[2]= nums[2]+nums[0]
        res = max(nums[1],nums[2])
        for i in range(3, len(nums)):
            nums[i]= max(nums[i-2]+nums[i], nums[i-3]+nums[i])
            res = max(res,nums[i])
        return res
        