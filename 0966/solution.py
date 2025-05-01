from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        ans = 0
        prefix = 0
        dd = defaultdict(lambda: 0)
        dd[0] = 1
        for n in nums:
            prefix += n
            ans += dd[prefix - goal]
            dd[prefix] += 1
        return ans