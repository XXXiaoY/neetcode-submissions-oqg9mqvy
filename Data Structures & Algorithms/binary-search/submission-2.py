class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if l < len(nums) and nums[l] == target:
            return l
        
        return -1