class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # 1. 创建 dp 数组，长度为 n+1
        # dp[i] 表示从下标 i 开始到结尾的解码方法数
        dp = [0] * (n + 1)
        
        # 2. 初始条件（相当于递归的 i == n）
        # 到达终点算 1 种方法
        dp[n] = 1
        
        # 3. 从后往前遍历
        for i in range(n - 1, -1, -1):
            # 情况 1：如果当前位是 '0'
            # 相当于 dfs 里的 if s[i] == '0': return 0
            if s[i] == '0':
                dp[i] = 0
                continue
            
            # 情况 2：先算“只取 1 位”
            # 相当于 res = dfs(i + 1)
            dp[i] = dp[i + 1]
            
            # 情况 3：再尝试“取 2 位”
            # 相当于 if ...: res += dfs(i + 2)
            if i + 1 < n:
                two_digit = int(s[i : i + 2])
                if 10 <= two_digit <= 26:
                    dp[i] += dp[i + 2]
                    
        # 4. 最终结果在 dp[0]
        return dp[0]
