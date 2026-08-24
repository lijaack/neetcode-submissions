class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        currSum=nums[0]

        for num in nums[1:]:
            if currSum < 0:
                currSum = num
            else:
                currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum
            