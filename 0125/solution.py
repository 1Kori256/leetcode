class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = "".join([c.lower() if c.isalnum() else "" for c in s])
        return x == x[::-1]