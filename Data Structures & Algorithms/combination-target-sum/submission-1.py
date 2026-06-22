class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        s = 0
        def dfs(i):
            nonlocal s
            if s == target:
                ans.append(path.copy())
                return
            if s > target:
                return
            
            for j in range(i ,len(nums)):
                path.append(nums[j])
                s += nums[j]
                dfs(j)
                path.pop()
                s -= nums[j]
        dfs(0)
        
        return ans

        