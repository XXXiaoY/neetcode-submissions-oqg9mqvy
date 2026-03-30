class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 特判：如果只有一间房，必须直接偷，不能走后面的拆分逻辑
        if n == 1:
            return nums[0]
            
        nums1 = nums[0:(len(nums)-1)]
        nums2 = nums[1:len(nums)]
        prev1= 0
        prev2 = 0
        for i in nums1:
            cur1 = max((prev2+i), prev1)
            prev2 = prev1
            prev1 = cur1
        prev1= 0
        prev2 = 0
        for i in nums2:
            cur2 = max((prev2+i), prev1)
            prev2 = prev1
            prev1 = cur2
        return max(cur1, cur2)
        
        