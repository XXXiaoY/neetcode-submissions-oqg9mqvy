class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        char  = defaultdict(int)

        for i in s1:
            char[i] += 1
        
        l = 0
        for r in range(len(s2)):
            val = s2[r]
            mp[val] += 1
            while r - l + 1 > len(s1):
                mp[s2[l]] -= 1
                if mp[s2[l]] == 0:
                    del mp[s2[l]]
                l += 1
            if char == mp:
                return True
        
        return False
            

        