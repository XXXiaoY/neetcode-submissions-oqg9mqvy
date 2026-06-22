class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = [False] * len(nums)
        nums.sort()
        def dfs():
            if len(path) == len(nums):
                ans.append(path.copy())
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                path.pop()
                used[i] = False
        dfs()
        
        return ans
        