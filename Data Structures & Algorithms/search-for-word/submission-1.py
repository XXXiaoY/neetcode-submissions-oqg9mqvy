class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # k 表示当前要匹配 word[k]

            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"   # 标记已访问，防止同一条路径重复使用

            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            board[i][j] = temp  # 回溯，恢复现场

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False