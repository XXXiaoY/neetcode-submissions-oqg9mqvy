class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # 协议：长度 + # + 内容
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num_start = j + 1
            num_len = int(s[i:j])
            res.append(s[num_start:num_start + num_len])
            i = num_start + num_len
        return res

            

