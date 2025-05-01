class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        my_hash = {nums[i]: set() for i in range(len(nums))}
        for i in range(len(nums)):
            my_hash[nums[i]].add(i)
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if -nums[i]-nums[j] in my_hash:
                    if any(x > max(i, j) for x in my_hash[-nums[i]-nums[j]].difference(set([i, j]))):
                        result.add(tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]])))
        result = [list(x) for x in result]
        return result