class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = abs(num) - 1
            if nums[num] < 0:
                res.append(num + 1)
            else:
                nums[num] = -1 * nums[num]
        return res