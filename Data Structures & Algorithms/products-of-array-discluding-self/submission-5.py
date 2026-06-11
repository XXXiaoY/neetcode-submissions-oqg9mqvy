class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [1] * len(nums) 

        for i in range(len(nums)):
            ans[i] = product
            product = product * nums[i]
        
        suf_product = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] = ans[j] * suf_product
            suf_product = suf_product * nums[j]
        
        return ans
        