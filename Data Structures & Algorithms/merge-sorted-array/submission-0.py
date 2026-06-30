class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1          # nums1 有效部分的最后一个元素
        p2 = n - 1          # nums2 的最后一个元素
        write = m + n - 1   # nums1 最后一个位置

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1

            write -= 1

        # 如果 nums2 还有剩余，需要拷贝到 nums1 前面
        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1