class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,t):
            if i == len(nums) and t==0:
                return 1
            if i >= len(nums):
                return 0
            if (i,t) in memo:
                return memo[(i,t)]
            add = dfs(i+1, t-nums[i])
            sub = dfs(i+1,t+nums[i])
            memo[(i,t)] = add+sub

            return memo[(i,t)]
        
        return dfs(0,target)

    