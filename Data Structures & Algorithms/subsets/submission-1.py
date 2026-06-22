class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            nonlocal ans, path
            ans.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)

        return ans
        

        