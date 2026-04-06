class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        mp = defaultdict(int)
        left = 0

        for right in range(len(s)):
            val = s[right]
            while mp[val] > 0:
                mp[s[left]] -= 1
                left += 1
            mp[val] += 1
            max_l = max(max_l, right - left + 1)
        
        return max_l

                

     

        