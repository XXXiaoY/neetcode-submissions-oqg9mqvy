class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            i_num = ord(i) - ord('a')
            count[i_num] += 1
            j_num = ord(j) - ord('a')
            count[j_num] -= 1
        for m in count:
            if m != 0:
                return False
        return True

        