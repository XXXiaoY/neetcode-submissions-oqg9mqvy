class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        p = 1

        for i in range(len(nums)):
            product[i] = p
            p = p * nums[i]
        
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= suf
            suf *= nums[i]
        
        return product

        