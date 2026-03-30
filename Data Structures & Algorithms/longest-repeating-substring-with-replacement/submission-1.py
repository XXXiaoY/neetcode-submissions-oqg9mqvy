class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_l = 0
        mp = defaultdict(int)
        for right in range(len(s)):
            val = s[right]
            mp[val] += 1
            max_freq = max(max_freq, mp[val])

            while right - left + 1 - max_freq > k:
                mp[s[left]] -= 1
                left += 1
            max_l = max(max_l, right - left + 1)
        
        return max_l
       

            


        