from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache

        def dp(i, flag):
            if i == 0:
                return -prices[0] if flag else 0 
            
            if flag:
                return max(dp(i - 1, False) - prices[i], dp(i - 1, True))
            else:
                return max(dp(i - 1, False), dp(i - 1, True) + prices[i])
        
        return dp(len(prices) - 1, False)
        