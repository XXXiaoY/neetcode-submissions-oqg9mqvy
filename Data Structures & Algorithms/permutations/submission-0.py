class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                ans.append(path.copy())
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                path.pop()
                used[i] = False
        dfs()
        
        return ans
        