class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)
        if t%2:
            return False
        t = t//2
        memo={}
        def dfs(i,r):
            if(r == 0):
                return True
            if i >= len(nums) or r<0:
                return False
            
            if (i,r) in memo:
                return memo[(i,r)]

            take = dfs(i+1,r-nums[i])
            skip = dfs(i+1,r)  
            memo[(i,r)] = take or skip
            return memo[(i,r)]


        return dfs(0,t)