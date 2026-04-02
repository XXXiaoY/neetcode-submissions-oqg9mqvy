class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 1
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur:
                ans += 1
            else:
                ans -= 1
                if ans == 0:
                    cur = nums[i]
                    ans = 1
        return cur


        