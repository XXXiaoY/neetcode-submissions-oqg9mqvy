class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        map = defaultdict(int)
        for right, val in enumerate(s):
            while map[val] != 0:
                map[s[left]] -= 1
                left += 1
            map[val] += 1
            max_len = max(max_len, right - left + 1)
        return max_len


        