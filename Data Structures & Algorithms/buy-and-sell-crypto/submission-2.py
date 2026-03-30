class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_min = prices[0]
        max_pro = 0
        for i in range(1, len(prices)):
            val = prices[i]
            if val > l_min:
                max_pro = max(max_pro, val - l_min)
            else:
                l_min = val
        return max_pro

        