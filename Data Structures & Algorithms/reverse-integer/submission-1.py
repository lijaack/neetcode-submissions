class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # Smallest 32-bit integer: -2^31
        MAX = 2147483647   # Largest 32-bit integer:  2^31 - 1

        res = 0

        while x:
            # Get the last digit of x.
            #
            # Example:
            # x = 123
            # digit = 3
            digit = int(math.fmod(x, 10))

            # Remove the last digit from x.
            #
            # x = 123 → x = 12
            x = int(x / 10)

            # Check if adding this digit would make
            # res larger than the 32-bit maximum.
            #
            # res * 10 + digit is what we are about to calculate.
            #
            # We check BEFORE doing it so res doesn't overflow.
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            # Same check for the 32-bit minimum.
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            # Add the digit to the reversed number.
            #
            # Example:
            # res = 12, digit = 3
            # res = 12 * 10 + 3
            #     = 123
            res = (res * 10) + digit

        return res