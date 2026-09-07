class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            # Ignore numbers that cannot be useful:
            # negatives, 0, and numbers greater than n.
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue

            # Number x belongs at index x - 1.
            # Example: 1 → index 0, 2 → index 1, 3 → index 2.
            index = nums[i] - 1

            # Swap the number into its correct position.
            # Check nums[i] != nums[index] to avoid getting
            # stuck swapping duplicate values forever.
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                # The value is already in the correct position,
                # or it is a duplicate, so move to the next index.
                i += 1

        # After rearranging, index i should contain i + 1.
        # The first position where this isn't true gives
        # us the first missing positive.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If every position contains its expected positive number,
        # then the first missing positive is n + 1.
        return n + 1
