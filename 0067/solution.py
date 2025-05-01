class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        s = ""
        l = max(len(a), len(b))
        a_r = l - len(a)
        b_r = l - len(b)
        a = a[::-1] + "0" * a_r
        b = b[::-1] + "0" * b_r
        for i in range(l):
            x = int(a[i])
            y = int(b[i])
            r = x + y + c
            s += str(r % 2)
            c = 1 if r > 1 else 0
        if c:
            s += "1"
        return s[::-1]
            