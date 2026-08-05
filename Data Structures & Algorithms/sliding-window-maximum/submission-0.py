from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []

        # Stores indexes of useful elements.
        # Values are kept in decreasing order:
        # largest value is always at the front.
        window_indices = deque()

        left = 0
        right = 0

        while right < len(nums):

            current_value = nums[right]

            # Remove smaller values from the back.
            # They can never become the maximum while
            # current_value is still in the window.
            while (
                window_indices
                and nums[window_indices[-1]] < current_value
            ):
                window_indices.pop()

            # Add the current index.
            window_indices.append(right)

            # Remove the front index if it has
            # moved outside the current window.
            if window_indices[0] < left:
                window_indices.popleft()

            # Once the window reaches size k,
            # the front contains the maximum.
            if right + 1 >= k:
                result.append(nums[window_indices[0]])
                left += 1

            right += 1

        return result