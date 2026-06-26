import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, l, r):
            if l >= r:
                return
            # 随机选一个 pivot 下标
            pivot_idx = random.randint(l, r)

            # 把随机 pivot 换到最右边
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = nums[r]
            i = l
            for j in range(i, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            quickSort(nums, l, i - 1)
            quickSort(nums,i + 1, r)


        quickSort(nums, 0, len(nums) - 1)
        return nums
        