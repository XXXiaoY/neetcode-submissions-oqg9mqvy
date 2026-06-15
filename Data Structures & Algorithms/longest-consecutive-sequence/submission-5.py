class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_l = 0
        for i in s:
            if i - 1 in s:
                continue
            l = 1
            j = i + 1
            while j in s:
                l += 1
                j += 1
            
            max_l = max(max_l, l)
        
        return max_l
            
        