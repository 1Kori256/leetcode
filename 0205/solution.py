class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        m = {}
        k = {}
        for c, d in zip(s, t):
            if c in m:
                if d != m[c]:
                    return False
            if d in k:
                if c != k[d]:
                    return False
            k[d] = c
            m[c] = d
        return True
        