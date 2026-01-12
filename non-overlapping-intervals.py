class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        lastIntervalIndex = 0
        remove = 0

        for i in range(1, len(intervals)):
            # If overlaps, remove
            if intervals[i][0] < intervals[lastIntervalIndex][1]:
                remove += 1
                if intervals[i][1] < intervals[lastIntervalIndex][1]:
                    lastIntervalIndex = i
            else:
                lastIntervalIndex = i

        return remove
