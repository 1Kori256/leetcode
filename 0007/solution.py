class Solution:
    def reverse(self, x: int) -> int:
        f = 1
        if x < 0:
            f = -1
            x = abs(x)
        rev = int(str(x)[::-1])
        if - 2 ** 31 > rev or rev > 2 ** 31 - 1:
            return 0
        else:
            return f * rev