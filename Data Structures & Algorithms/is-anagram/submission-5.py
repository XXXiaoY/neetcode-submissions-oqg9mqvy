class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        char = [0] * 26
        for i, j in zip(s, t):
            char[ord(i) - ord('a')] += 1
            char[ord(j) - ord('a')] -= 1
        
        for m in char:
            if m != 0:
                return False
        
        return True
        