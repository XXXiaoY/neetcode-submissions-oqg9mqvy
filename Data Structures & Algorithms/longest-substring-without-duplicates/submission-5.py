class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        l = 0
        max_l = 0
        for i in range(len(s)):
            val = s[i]
            while mp[val] != 0:
                mp[s[l]] -= 1
                l += 1
            max_l = max(max_l, i - l + 1)
            mp[val] += 1
        
        return max_l
        