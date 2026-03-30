from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_l = float('inf')
        start = 0

        left = 0
        right = 0

        t_count = Counter(t)
        mp = defaultdict(int)

        process = defaultdict(int)
        for ch in t:
            process[ch] += 1
        need = len(process)   # 还有多少种字符没满足

        while right < len(s):
            val = s[right]
            mp[val] += 1

            if val in t_count:
                process[val] -= 1
                if process[val] == 0:
                    need -= 1

            while need == 0:
                if right - left + 1 < min_l:
                    min_l = right - left + 1
                    start = left

                left_ch = s[left]
                mp[left_ch] -= 1

                if left_ch in t_count:
                    process[left_ch] += 1
                    if process[left_ch] == 1:
                        need += 1

                left += 1

            right += 1

        return "" if min_l == float('inf') else s[start:start + min_l]