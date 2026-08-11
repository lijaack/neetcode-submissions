class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # Find where both bits are 1.
            # 1 + 1 creates a carry.
            # << 1 moves the carry one position to the left.
            carry = (a & b) << 1

            # XOR adds the numbers without carrying.
            #
            # Example:
            #   0111
            # ^ 0011
            # -------
            #   0100
            #
            # The carry is handled separately above.
            #
            # & mask keeps only the lower 32 bits
            # because Python integers are not fixed to 32 bits.
            a = (a ^ b) & mask

            # The carry becomes the new b.
            # We repeat the process until there is no carry left.
            b = carry & mask

        # If a is within the positive 32-bit range,
        # it is already the correct answer.
        #
        # Otherwise, the 32-bit pattern represents
        # a negative number, so convert it back to
        # Python's negative integer representation.
        return a if a <= max_int else ~(a ^ mask)