class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def findIn(start, end):
            if start >= end:
                return start
            pos = (start + end) // 2
            if nums[pos] == target:
                return pos
            elif nums[pos] > target:
                return findIn(start, pos)
            else:
                return findIn(pos + 1, end)
        return findIn(0, len(nums))