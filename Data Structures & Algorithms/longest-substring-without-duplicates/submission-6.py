class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            val = s[r]
            while mp[val] > 0:
                mp[s[l]] -= 1
                l += 1
            mp[val] += 1
            longest = max(longest, r - l + 1)
        
        return longest
            

        