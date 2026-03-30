class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        mp = defaultdict(int)
        for right, val in enumerate(s):
            while mp[val] > 0:
                mp[s[left]] -=  1
                left += 1
            max_length = max(max_length, right - left + 1)
            mp[val] += 1
        return max_length
        