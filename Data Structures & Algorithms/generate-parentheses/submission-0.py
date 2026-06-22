class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, path = [], []
        def dfs(left, right):
            if len(path) == 2 * n:
                ans.append(''.join(path))
                return
            if left < n:            # 左括号还没用完
                path.append('(')
                dfs(left + 1, right)
                path.pop()
            if right < left:        # 右括号数量必须小于左括号
                path.append(')')
                dfs(left, right + 1)
                path.pop()
        dfs(0, 0)
        return ans
            

        