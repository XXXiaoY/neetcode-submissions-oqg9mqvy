class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        minimum = float('inf')
        for i in prices:
            max_prof = max(max_prof, i - minimum)
            minimum = min(minimum, i)
        
        return max_prof