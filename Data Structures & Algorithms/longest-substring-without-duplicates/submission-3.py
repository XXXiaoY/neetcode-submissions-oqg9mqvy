class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        mp = defaultdict(int)
        l = 0
        for r in range(len(s)):
            val = s[r]
            while mp[val] > 0:
                mp[s[l]] -= 1
                l += 1
            mp[val] += 1
            max_l = max(max_l, r - l + 1)
        
        return max_l
        