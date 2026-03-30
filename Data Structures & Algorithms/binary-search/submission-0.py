class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1  # 范围缩小到 [mid+1, right]
            else:
                right = mid - 1  # 范围缩小到 [left, mid-1]

        
        return left if left < len(nums) and nums[left] == target else -1

        