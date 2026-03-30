class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x:x[0])
        ans = []
        for s, e in intervals:
            if not ans or ans[-1][1] < s:
                ans.append([s,e])
            else:
                ans[-1][1] = max(ans[-1][1], e)
        return ans
    
        