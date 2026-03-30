class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_l = 0
        for i, val in enumerate(nums):
            if i > max_l:
                break
            max_l = max(max_l,i + val)
        if max_l >= len(nums) - 1:
            return True
        return False

