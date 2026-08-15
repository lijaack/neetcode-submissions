class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Store all completed permutations
        self.res = []

        # Start with an empty permutation.
        # pick[i] tells us whether nums[i] is already being used.
        self.backtrack([], nums, [False] * len(nums))

        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):

        # We have picked every number.
        # Save a copy because perm will continue changing during backtracking.
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        # Try every number as the next number in the permutation
        for i in range(len(nums)):

            # If this number hasn't been used yet, we can choose it
            if not pick[i]:

                # MAKE THE CHOICE
                perm.append(nums[i])

                # Mark this specific index as used
                pick[i] = True

                # EXPLORE everything that can come after this choice
                self.backtrack(perm, nums, pick)

                # UNDO THE CHOICE
                # Remove the number we just added
                perm.pop()

                # Make this number available again
                # so another branch can use it
                pick[i] = False