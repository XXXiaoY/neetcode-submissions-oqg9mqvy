class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_s = 0
        s = 0
        ans = -1001

        for i in nums:
            s += i
            ans = max(ans, s - min_s)
            min_s = min(min_s, s)

        return ans
        