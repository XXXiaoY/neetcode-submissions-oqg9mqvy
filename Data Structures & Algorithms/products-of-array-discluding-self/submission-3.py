class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1 
        pre_product = [1] * len(nums)
        for i in range(1, len(nums)):
            pre = pre * nums[i - 1]
            pre_product[i] = pre
        suf = 1
        for j in range(len(nums) - 2, - 1, -1):
            suf = suf * nums[j + 1]
            pre_product[j] = suf * pre_product[j]
        return pre_product



