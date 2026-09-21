class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)
        if t%2:
            return False
        t=t//2
        memo={}
        def dfs(i, remaining):
            # We found a subset that adds up to the target
            if remaining == 0:
                return True

            # No numbers left, but we haven't reached the target
            if i == len(nums) or remaining < 0:
                return False

            # Return cached result if we've already solved this state
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Option 1: Include nums[i]
            take = dfs(i + 1, remaining - nums[i])

            # Option 2: Skip nums[i]
            skip = dfs(i + 1, remaining)

            # Either choice can lead to a valid subset
            memo[(i, remaining)] = take or skip

            return memo[(i, remaining)]

        return dfs(0, t)
