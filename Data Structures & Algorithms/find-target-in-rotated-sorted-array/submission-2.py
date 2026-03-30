class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = -1
        right = n
        while left + 1 < right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            # mid and its left side is sorted
            if nums[mid] >= nums[0]:
                if nums[0] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[n-1]:
                    left = mid   # target 在右段且在 mid 右边
                else:
                    right = mid
             
        return -1
        