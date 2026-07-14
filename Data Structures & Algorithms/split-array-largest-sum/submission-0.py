class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def canSplit(limit):
            count = 1
            cur = 0

            for x in nums:
                if cur + x > limit:
                    count += 1
                    cur = x
                else:
                    cur += x

            return count <= k

        while l < r:
            mid = (l + r) // 2

            if canSplit(mid):
                r = mid
            else:
                l = mid + 1

        return l