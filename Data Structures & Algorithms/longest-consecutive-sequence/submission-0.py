class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        l = 0

        for i in st:
            if (i - 1) in st:
                continue
            y = i + 1
            while y in st:
                y += 1
            l = max(l,y-i)
                
        
        return l
        