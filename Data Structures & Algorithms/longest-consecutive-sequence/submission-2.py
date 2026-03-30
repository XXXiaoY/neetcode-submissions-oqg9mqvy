class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for i in st:
            j = 1
            if i - 1 in st:
                continue
            m = i + 1
     
            while  m in st:
                j += 1
                m += 1

            ans = max(ans, j)
        return ans


        