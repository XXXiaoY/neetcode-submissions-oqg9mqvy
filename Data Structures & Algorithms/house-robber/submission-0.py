class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2 相当于 dp[i-2]，prev1 相当于 dp[i-1]
        prev2 = 0
        prev1 = 0
        
        for x in nums:
            # 这里的 temp 就像是计算出的当前 dp[i]
            # 计算完后，窗口向右滚动
            temp = max(prev1, x + prev2)
            prev2 = prev1
            prev1 = temp
            
        return prev1

        