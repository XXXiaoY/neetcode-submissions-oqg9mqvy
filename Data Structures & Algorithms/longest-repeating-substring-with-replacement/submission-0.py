class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mp = defaultdict(int)
        max_f = 0 
        max_l = 0
        for right, val in enumerate(s):
            mp[val] += 1
            max_f = max(max_f, mp[val])
            if right - left + 1 - max_f > k:
                mp[s[left]] -= 1
                left += 1
            max_l = max(max_l, right - left + 1)
        return max_l
            
    

                    
                        
                

        