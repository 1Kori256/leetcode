class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        right = 0
        ans = 0

        status = {x: False for x in set([c for c in s])}

        while right < len(s):
            if status[s[right]] == False:
                status[s[right]] = True
                right += 1
                ans = max(ans, right - left)
            else:
                while left < right:
                    status[s[left]] = False
                    if s[left] == s[right]:
                        status[s[right]] = True
                        left += 1
                        right += 1
                        break
                    left += 1
        return ans