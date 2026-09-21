class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1

            for j in range(i,len(nums)):
                if nums[j] > nums[i]:
                    res = max(dfs(j)+1, res)
            memo[i] = res

            return memo[i] 
        res = 0

        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res
