class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    # dfs(n) = min(dfs(n - coins[i]) + 1)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount + 1):
            for val in coins:
                if i - val >= 0:
                    dp[i] = min(dp[i], dp[i - val] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
                
        

        