class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_in = float('inf')

        for i in prices:
            max_p = max(max_p, i - min_in)
            min_in = min(min_in, i)
        
        return max_p
        