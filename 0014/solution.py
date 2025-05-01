class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(min(len(x) for x in strs)):
            if len(set(s[i] for s in strs)) != 1:
                return strs[0][:i]
        return strs[0][:min(len(x) for x in strs)]