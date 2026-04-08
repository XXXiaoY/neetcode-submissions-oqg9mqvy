class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mp = defaultdict(int)
        for p, on, out in trips:
            mp[on] += p
            mp[out] -= p
        
        mp = sorted(mp.items(), key = lambda x:x[0] )
        s = 0
        max_v = 0

        for i, vol in mp:
            s += vol
            max_v = max(max_v, s)
        
        return True if max_v <= capacity else False


            
        