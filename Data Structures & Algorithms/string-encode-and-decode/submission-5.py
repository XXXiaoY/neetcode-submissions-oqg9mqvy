class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for i in strs:
            ans.append(str(len(i)))
            ans.append('#')
            ans.append(i)
        return ''.join(ans)


    def decode(self, s: str) -> List[str]:
        i = j = 0
        ans = []
        while i < len(s):
            while s[i] != '#':
                i += 1
            l = int(s[j:i])   # 先取长度，此时 i 指向 '#'
            i += 1            # 跳过 '#'

            word = s[i : i + l]
            ans.append(word)
            j = i + l
            i = j
        return ans
