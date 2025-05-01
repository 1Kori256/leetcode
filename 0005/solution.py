class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = 0
        index1, index2 = 0, 0
        for i in range(len(s)):
            for start, end in [(i, i), (i, i + 1)]:
                if end == len(s):
                    break
                while s[start] == s[end]:
                    if end - start + 1 > ans:
                        ans = end - start + 1
                        index1 = start
                        index2 = end
                    start -= 1
                    end += 1
                    if start < 0 or end >= len(s):
                        break
        
        return s[index1:index2 + 1]