class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        n = len(candidates)
        cur_sum = 0

        def dfs(i : int):
            nonlocal cur_sum
            if cur_sum == target:
                ans.append(path.copy())
                return
            if cur_sum > target:
                return
            for j in range(i, n):
                cur_sum += candidates[j]
                path.append(candidates[j])
                dfs(j)
                path.pop()
                cur_sum -= candidates[j]

        dfs(0)
        return ans

        