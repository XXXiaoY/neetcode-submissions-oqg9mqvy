class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = defaultdict(int)
        td = defaultdict(int)
        for i,j in zip(s, t):
            sd[i] += 1
            td[j] += 1
        return sd == td
        