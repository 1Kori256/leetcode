class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=j=0
        cp = 1
        ans = 0
        while i<len(nums) and j<len(nums):
            if i == j:
                if nums[i] >= k:
                    i+=1
                    j+=1
                    cp = 1

                else:
                    j+=1
                    cp*=nums[i]
            else:
                if cp * nums[j] >= k:
                    ans += j - i
                    cp /= nums[i]
                    i+=1
                else:
                    cp *= nums[j]
                    j+=1
        ans += (j - i) * (j - i + 1) // 2
        return ans
        