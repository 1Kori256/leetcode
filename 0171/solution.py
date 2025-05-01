class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans *= 26
            ans += ord(c) - 64
        return ans