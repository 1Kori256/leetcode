class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            x = self.permuteUnique(nums[:i] + nums[i+1:])
            for d in x:
                result.append([nums[i]] + d)
        return result