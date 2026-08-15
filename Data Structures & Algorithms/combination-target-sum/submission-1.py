class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # Sort so we can stop early when a number makes total > target
        nums.sort()

        def dfs(i, cur, total):

            # We reached the target, so save this combination
            if total == target:
                res.append(cur.copy())
                return

            # Try every possible number starting from index i
            for j in range(i, len(nums)):

                # Since nums is sorted, everything after nums[j]
                # will also be too large, so stop searching this branch
                if total + nums[j] > target:
                    return

                # Choose nums[j]
                cur.append(nums[j])

                # Recurse using j (NOT j + 1)
                # This allows us to use the same number again
                dfs(j, cur, total + nums[j])

                # Undo our choice so we can try the next number
                cur.pop()

        # Start at index 0 with an empty combination and total of 0
        dfs(0, [], 0)

        return res