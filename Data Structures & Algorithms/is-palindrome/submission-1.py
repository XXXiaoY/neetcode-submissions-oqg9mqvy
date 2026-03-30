class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l = l + 1
            elif not s[r].isalnum():
                r = r - 1
            elif s[l].lower() == s[r].lower():
                l = l + 1
                r = r - 1
            else:
                return False
        return True
        