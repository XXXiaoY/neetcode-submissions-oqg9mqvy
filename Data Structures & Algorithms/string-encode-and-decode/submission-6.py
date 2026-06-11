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
            num = int(s[i:j]) #[2#ab3#abb]
            i = j + 1 + num

            st = s[j + 1:i]
            ans.append(st)
        
        return ans
