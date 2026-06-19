class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2

            hour = 0
            for i in piles:
                hour += (i + mid - 1) // mid
            if hour <= h:
                r = mid
            else:
                l = mid + 1
        
        return l

        