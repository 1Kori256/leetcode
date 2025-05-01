class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for i in range(len(nums)):
            x = self.permute(nums[:i] + nums[i+1:])
            for d in x:
                result.append([nums[i]] + d)
        return result