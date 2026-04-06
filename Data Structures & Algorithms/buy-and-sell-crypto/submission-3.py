class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell = float('inf')
        max_prof = 0
        for i in prices:
            max_prof = max(max_prof, i - min_sell)
            min_sell = min(min_sell, i)
        
        return max_prof

        