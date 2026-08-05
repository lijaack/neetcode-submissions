class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort so we can use two pointers and skip duplicates
        nums.sort()
        # Fix the first number
        for i, first in enumerate(nums):
            # If the smallest possible first number is positive,
            # three positive numbers can never sum to zero
            if first > 0:
                break
            # Skip duplicate first numbers
            if i > 0 and first == nums[i - 1]:
                continue
            # Find two numbers that add up to -first
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = first + nums[left] + nums[right]
                if total > 0:
                    # Sum is too large, decrease right value
                    right -= 1
                elif total < 0:
                    # Sum is too small, increase left value
                    left += 1
                else:
                    # Found a valid triplet
                    res.append([first, nums[left], nums[right]])
                    # Move both pointers to look for more answers
                    left += 1
                    right -= 1
                    # Skip duplicate second numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res