class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # 1. Take bit i from n
            bit = (n >> i) & 1

            # 2. Put it in the opposite position
            res += (bit << (31 - i))
        return res