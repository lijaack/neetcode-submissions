class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n + 1):
            one = 0

            # Check each of the 32 bit positions.
            #
            # (1 << i) creates a 1 at position i.
            #
            # Example: num = 5
            # 5 = 101
            #
            # i = 0:
            # 1 << 0 = 001
            # 101 & 001 = 001 → found a 1 → one = 1
            #
            # i = 1:
            # 1 << 1 = 010
            # 101 & 010 = 000 → no 1 → one stays 1
            #
            # i = 2:
            # 1 << 2 = 100
            # 101 & 100 = 100 → found a 1 → one = 2
            #
            # So 5 has two 1-bits.
            for i in range(32):
                if num & (1 << i):
                    one += 1

            # Store the number of 1-bits for this number.
            res.append(one)

        return res