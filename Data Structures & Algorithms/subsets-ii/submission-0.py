class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        def dfs(i):
            nonlocal ans, path

            ans.append(path.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        
        dfs(0)
        
        return ans