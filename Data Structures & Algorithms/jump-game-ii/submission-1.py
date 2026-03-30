class Solution:
    def jump(self, nums: List[int]) -> int:
        next_maxj = 0
        max_l = 0
        count = 0
        for i in range(len(nums) - 1):
            next_maxj = max(next_maxj, i + nums[i])
            if i == max_l:
                max_l = next_maxj
                count += 1
            
        return count

        