class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            # n & (n - 1) removes the rightmost 1-bit.
            #
            # Example: n = 101100
            #
            # n     = 101100
            # n - 1 = 101011
            #
            #       101100
            #     & 101011
            #       ------
            #       101000
            #
            # The rightmost 1 was removed.
            #
            # Each time we do this, we remove one 1-bit,
            # so increase the count by 1.
            n = n & (n - 1)
            res += 1

        return res