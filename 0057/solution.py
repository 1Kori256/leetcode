class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        start_index = 0
        start = newInterval[0]
        for i in range(len(intervals) - 1, -1, - 1):
            if intervals[i][0] <= newInterval[0]:
                if intervals[i][1] < newInterval[0]:
                    start_index = i + 1
                    start = newInterval[0]
                else:
                    start = min(intervals[i][0], newInterval[0])
                    start_index = i
                break
        newInterval[0] = start
        print(start_index)
        intervals.insert(start_index, newInterval)
        print(intervals)
        x = start_index + 1
        while x < len(intervals):
            if intervals[x][0] <= newInterval[1]:
                intervals[start_index][1] = max(intervals[start_index][1], intervals[x][1])
                del intervals[x]
            else: 
                x  += 1
        return intervals   