class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for i in strs:
            ans.append(str(len(i)))
            ans.append('#')
            ans.append(i)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            cur_l = int(s[i:j])
            ans.append(s[j+1:j+cur_l+1])
            i = j + cur_l + 1
        return ans

