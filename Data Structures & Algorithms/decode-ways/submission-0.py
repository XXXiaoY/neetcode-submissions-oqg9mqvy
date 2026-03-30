class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):

            # 单字符
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # 双字符
            cur = int(s[i-2:i])
            if 10 <= cur <= 26:
                dp[i] += dp[i-2]

        return dp[n]

        