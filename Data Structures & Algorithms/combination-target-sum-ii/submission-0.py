class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        s = 0
        candidates.sort()
        def dfs(i):
            nonlocal s
            if s == target:
                ans.append(path.copy())
                return
            if s > target:
                return
            
            for j in range(i ,len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                s += candidates[j]
                dfs(j + 1)
                path.pop()
                s -= candidates[j]
        dfs(0)
        
        return ans