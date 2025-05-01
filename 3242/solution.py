from collections import Counter
from functools import reduce
from operator import mul

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(mul, max(Counter(list(Counter(nums).values())).items(), key=lambda x: x[0]))