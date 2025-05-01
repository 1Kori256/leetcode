class Solution:
    def isHappy(self, n: int) -> bool:
        found = set([n])
        while n != 1:
            n = self.reduce(n)
            if n in found:
                return False
            found.add(n)
        return True

    def reduce(self, n):
        return sum([int(x) * int(x) for x in str(n)])