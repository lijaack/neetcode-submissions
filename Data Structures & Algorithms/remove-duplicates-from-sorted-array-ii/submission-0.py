class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                j = i + 2
                cnt = 0
                while j < n and nums[i] == nums[j]:
                    j += 1
                    cnt += 1
                for k in range(i + 2, n):
                    if j >= n:
                        break
                    nums[k] = nums[j]
                    j += 1
                n -= cnt
                i += 2
            else:
                i += 1
        return n        