class Solution:
    def pivotInteger(self, n: int) -> int:
        import math
        x = math.sqrt(n*(n+1)/2)
        if abs(x-round(x))<0.001:
            return round(x)
        return -1