class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. 先把 res 当作 prefix 数组用
        # res[i] 存储 i 左边所有数的积
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
            
        # 2. 从右往左扫，动态维护右边的累乘积
        right_product = 1
        for i in range(n - 1, -1, -1):
            # 此时 res[i] 是左积，乘以当前的右积
            res[i] = res[i] * right_product
            # 更新右积，供下一个（左边的一个）位置使用
            right_product *= nums[i]
            
        return res
            

        