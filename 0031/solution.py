class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        my_indx = -1
        for i in range(n - 2, -1 , -1):
            if nums[i] < nums[i + 1]:
                my_indx = i
                break
        smallest_larger = 101
        smallest_larger_index = -1
        for i in range(my_indx + 1, n):
            if nums[i] > nums[my_indx] and nums[i] <= smallest_larger:
                smallest_larger = nums[i]
                smallest_larger_index = i
        if my_indx >= 0:
            nums[my_indx], nums[smallest_larger_index] = nums[smallest_larger_index], nums[my_indx]
        for i in range(my_indx + 1, n):
            j = n - (i - my_indx)
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]