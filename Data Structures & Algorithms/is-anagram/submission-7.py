class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = [0] * 26

        for i, j in zip(s, t):
            check[ord(i) - ord('a')] += 1
            check[ord(j) - ord('a')] -= 1
        
        for m in check:
            if m != 0:
                return False
        
        return True
        