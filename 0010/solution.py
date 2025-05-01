class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        prev_star = False
        np = ""
        for c in p:
            if c != "*":
                prev_star = False
                np += c
            else:
                if not prev_star:
                    np += "*"
                prev_star = True
        if re.match("^" + np + "$", s):
            return True
        return False