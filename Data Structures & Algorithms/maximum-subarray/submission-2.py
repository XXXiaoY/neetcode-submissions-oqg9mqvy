class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        min_s = 0
        max_sum = float('-inf')

        for i in nums:
            s += i
            if s - min_s > max_sum:
                max_sum = s - min_s
            min_s = min(min_s, s)
        
        return max_sum
        