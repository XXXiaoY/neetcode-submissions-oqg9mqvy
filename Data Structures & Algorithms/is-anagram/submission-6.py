class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        verify = [0] * 26
        if len(s) != len(t):
            return False
        
        for i,j in zip(s, t):
            verify[ord(i) - ord('a')] += 1
            verify[ord(j) - ord('a')] -= 1
        
        for m in verify:
            if m != 0:
                return False

        return True 
        