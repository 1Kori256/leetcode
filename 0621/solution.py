from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f = sorted([v for k, v in Counter(tasks).items()])
        f_c = len([x for x in f if x == max(f)])
        return max((n + 1) * (max(f) - 1) + f_c, len(tasks))