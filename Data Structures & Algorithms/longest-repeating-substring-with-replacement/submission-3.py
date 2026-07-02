class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f = 0
        max_l = 0
        l = 0
        mp = defaultdict(int)
        for r in range(len(s)):
            mp[s[r]] += 1
            max_f = max(max_f, mp[s[r]])
            while (r - l + 1) - max_f > k:
                mp[s[l]] -= 1
                l += 1
            max_l = max(max_l, r - l + 1)
        
        return max_l

        