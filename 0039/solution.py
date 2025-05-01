class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        def rec(indx, target):
            if indx >= len(candidates):
                return None
            res = []
            for i, c in enumerate(candidates[indx:]):
                if target == c:
                    res.append([c])
                    break
                if c > target:
                    continue
                x = rec(i + indx, target - c)
                if x is None:
                    continue
                for s in x:
                    res.append(s + [c])
            return res

        return rec(0, target)