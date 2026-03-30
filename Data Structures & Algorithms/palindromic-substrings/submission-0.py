class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        #odd
        l = 0
        r = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        l1 = 0
        r1 = 0
        for i in range(n):
            l1 = i
            r1 = i + 1
            while l1 >= 0 and r1 < len(s) and s[l1] == s[r1]:
                count += 1
                l1 -= 1
                r1 += 1

        return count

            


        