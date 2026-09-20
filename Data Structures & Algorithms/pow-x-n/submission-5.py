class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n:
            # If n is odd, use the current x
            if n % 2 == 1:
                result *= x

            # Square x
            x *= x

            # Cut exponent in half
            n //= 2

        return result