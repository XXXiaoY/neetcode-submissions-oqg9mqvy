class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left <= right:
            mid = (right + left) // 2
            hour = 0
            for i in piles:
                if mid >= i:
                    hour += 1
                else:
                    hour += (i + mid - 1) // mid

                   
            if hour > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left