class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key = lambda x:x[1])
        end = float('-inf')

        for s, e in intervals:
            if s >= end:
                end = e
            else:
                cnt += 1
        
        return cnt

        