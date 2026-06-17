class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char = defaultdict(int)
        mp = defaultdict(int)
        for i in t:
            char[i] += 1
        need = len(char)
        min_l = 0
        min_r = float('inf')


        l = 0
        for r in range(len(s)):
            val = s[r]
            char[val] -= 1
            if char[val] == 0:
                need -= 1
                while need == 0:
                    if r - l < min_r - min_l:
                        min_r, min_l = r, l
                    l_val = s[l]
                    char[l_val] += 1
                    if char[l_val] > 0:
                        need += 1
                    l += 1
        
        return "" if min_r == float('inf') else s[min_l : min_r + 1]
        

        

        