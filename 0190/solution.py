from functools import reduce

class Solution:
    def reverseBits(self, n: int) -> int:
            return reduce(lambda x, y: x | y, [((n >> i) & 1) << 31 - i for i in range(32)])