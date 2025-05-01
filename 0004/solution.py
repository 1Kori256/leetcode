class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        merged = sorted(nums1 + nums2)
        total = len(merged)
        if total % 2 == 1:
            return merged[total // 2]
        return (merged[total // 2 - 1] + merged[total // 2]) / 2.0