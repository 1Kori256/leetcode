class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        x = {}
        for i, e in enumerate(nums):
            if target - e in x:
                return x[target - e], i
            x[e] = i