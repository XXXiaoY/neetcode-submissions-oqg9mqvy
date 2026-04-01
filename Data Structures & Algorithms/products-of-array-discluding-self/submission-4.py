class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums) 
        s = 1
        for i in range(len(nums)):
            if i > 0:
                s = s * nums[i - 1]
            ans[i] = s

        suf = 1
        for j in range(len(nums) - 1, -1, -1):
            if j < len(nums) - 1:
                suf = suf * nums[j + 1]
            ans[j] = ans[j] * suf
        
        return ans

    # loop1: 
    # ans[1,1,2,8]
    # loop2:
    # ans[48,24,12,8]