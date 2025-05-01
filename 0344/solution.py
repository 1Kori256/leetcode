class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
        while i < len(s)-i-1:
            s[i], s[n-i-1] = s[n-i-1], s[i]
            i += 1