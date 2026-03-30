class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) in numSet:
                continue
            j = i + 1
            while j in numSet:
                j += 1
            longest = max(longest, j - i)
        return longest


        
        

        