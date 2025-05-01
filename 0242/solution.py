class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnts_s = {}
        cnts_t = {}
        for c in s:
            cnts_s[c] = cnts_s.get(c, 0) + 1
        for c in t:
            cnts_t[c] = cnts_t.get(c, 0) + 1
        if len(cnts_s) != len(cnts_t):
            return False
        for c in cnts_s:
            if cnts_s[c] != cnts_t.get(c, -1):
                return False
        return True