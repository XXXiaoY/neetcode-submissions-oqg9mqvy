class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_l = 0
        s = set(nums)

        for i in s:
            if (i - 1) in nums:
                continue
            else:
                j = i + 1
                l = 1
                while j in s:
                    l += 1
                    j += 1
                max_l = max(max_l, l)
        
        return max_l


        