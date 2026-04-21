class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, val in enumerate(nums):
            res ^= i ^ val
        
        return res
        