class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # Example: nums = [2, 3, 2]
            #
            # XOR rule:
            # Same bits → 0
            # Different bits → 1
            #
            # Start:
            # res = 0
            #
            # num = 2:
            # res = 2 ^ 0
            #     = 10 ^ 00
            #     = 10 = 2
            #
            # num = 3:
            # res = 3 ^ 2
            #     = 11 ^ 10
            #     = 01 = 1
            #
            # num = 2:
            # res = 2 ^ 1
            #     = 10 ^ 01
            #     = 11 = 3
            #
            # The duplicate 2s cancel:
            # 2 ^ 3 ^ 2
            # = 2 ^ 2 ^ 3
            # = 0 ^ 3
            # = 3
            #
            # So the number that appears once remains.
            res = num ^ res

        return res