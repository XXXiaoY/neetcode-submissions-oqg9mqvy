class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return 1
            
            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0
            
            # 可能性 1：只解码当前这 1 位
            # 既然 s[i] 不是 '0'，那它一定能代表 A-I 中的一个
            res = dfs(i + 1)

            if i + 1 < n:
                # 把字符串转成数字判断，比如 "2" + "6" -> 26
                two_digit = int(s[i : i + 2])
                if 10 <= two_digit <= 26:
                    res += dfs(i + 2)
            
            memo[i] = res
            return res

        return dfs(0)