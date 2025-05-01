class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        final = (m + n - 1)
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[final] = nums1[i1]
                i1 -= 1
            else:
                nums1[final] = nums2[i2]
                i2 -= 1
            final -= 1
        for i in range(i2 + 1):
            nums1[i] = nums2[i]
