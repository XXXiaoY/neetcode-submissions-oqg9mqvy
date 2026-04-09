class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1

        while left < right:
            mid = (left + right) // 2
            hour = 0
            for i in piles:
                hour += (i + mid - 1) // mid 
            
            if hour > h:
                left = mid + 1
            else:
                right = mid
        
        return left

        