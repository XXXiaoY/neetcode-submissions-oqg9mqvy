class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        end = float('-inf')
        count = 0
        for s,e in intervals:
            if s >= end:
                count += 1
                end = e
        return len(intervals) - count



        