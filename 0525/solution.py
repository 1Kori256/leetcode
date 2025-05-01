class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        x = {0: -1}
        s = 0
        ans = 0
        for i, num in enumerate(nums):
            s += num * 2 - 1
            if s in x:
                ans = max(ans, i - x[s])
            else:
                x[s] = i
        return ans