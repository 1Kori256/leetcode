class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        x = list(set(nums))
        x.sort()
        for i, e in enumerate(x):  
            nums[i] = e
        return len(x)