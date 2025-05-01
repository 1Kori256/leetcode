class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for x in strs:
            u = "".join(sorted(i for i in x))
            if u in ans:
                ans[u].append(x)
            else:
                ans[u] = [x]
        return list(ans.values())