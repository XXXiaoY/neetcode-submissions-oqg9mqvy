class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        t_n = Counter(t)
        s_n = Counter()

        left_ans, right_ans = -1, len(s)

        for right, val in enumerate(s):
            s_n[val] += 1
            while s_n >= t_n:
                if right - left < right_ans - left_ans:
                    left_ans, right_ans = left, right
                s_n[s[left]] -= 1
                left += 1
        return "" if left_ans < 0 else s[left_ans: right_ans+1] 
        