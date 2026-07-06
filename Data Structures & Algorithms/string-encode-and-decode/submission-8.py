class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for i in strs:
            ans.append(str(len(i)))
            ans.append('#')
            ans.append(i)

        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            s_cut = s[j + 1: j + 1 + l] #[2#ad5#]
            ans.append(s_cut)
            i = j + 1 + l
        
        return ans

            


