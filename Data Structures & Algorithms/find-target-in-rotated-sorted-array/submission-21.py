class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found the target
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target is NOT inside the sorted left half
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1

                # Target is inside the sorted left half
                else:
                    right = mid - 1

            # Right half is sorted
            else:

                # Target is NOT inside the sorted right half
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1

                # Target is inside the sorted right half
                else:
                    left = mid + 1

        return -1