class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        for i in t:
            mp[i] += 1
        need = len(mp)
        left = 0

        l_min = 0
        r_min = float('inf')

        for right in range(len(s)):
            val = s[right]
            mp[val] -= 1
            if mp[val] == 0:
                need -= 1
                while need == 0:
                    if right - left < r_min - l_min:
                        l_min, r_min = left, right
                    l_val = s[left]
                    if mp[l_val] == 0:
                        need += 1
                    mp[l_val] += 1
                    left += 1
        return s[l_min:r_min + 1] if r_min != float('inf') else ""
        