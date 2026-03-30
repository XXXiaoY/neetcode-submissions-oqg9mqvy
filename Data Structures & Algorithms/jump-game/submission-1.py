class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_j = 0
        for i, val in enumerate(nums):
            if i > max_j:
                return False
            max_j = max(max_j, i + val)
        return True
        

        