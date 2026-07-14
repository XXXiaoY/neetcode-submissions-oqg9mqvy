class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def countDay(capacity):
            day = 1
            cur = 0

            for w in weights:
                if cur + w > capacity:
                    day += 1
                    cur = w
                else:
                    cur += w

            return day

        while l < r:
            mid = (l + r) // 2
            d = countDay(mid)

            if d > days:
                l = mid + 1
            else:
                r = mid

        return l