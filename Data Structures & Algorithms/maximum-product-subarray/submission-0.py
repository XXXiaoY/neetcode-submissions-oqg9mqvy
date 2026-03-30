class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] 到index i 的最大
        # 选： dp[i - 1] * dp[i]
        # 不选  dp[i - 1]
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            temp_max = max(num, num * max_prod, num * min_prod)
            temp_min = min(num, num * max_prod, num * min_prod)

            max_prod = temp_max
            min_prod = temp_min

            res = max(res, max_prod)

        return res