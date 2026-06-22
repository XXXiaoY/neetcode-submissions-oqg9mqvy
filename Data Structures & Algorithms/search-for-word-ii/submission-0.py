class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # 如果这里是某个单词结尾，就存这个完整单词


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # 1. 建 Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        m, n = len(board), len(board[0])
        ans = []

        def dfs(i, j, node):
            ch = board[i][j]

            # 当前格子的字符不在 Trie 路径里，直接剪枝
            if ch not in node.children:
                return

            node = node.children[ch]

            # 如果当前 Trie 节点是某个单词结尾，加入答案
            if node.word is not None:
                ans.append(node.word)
                node.word = None   # 防止重复加入同一个单词

            # 标记当前格子已访问
            board[i][j] = "#"

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                    dfs(x, y, node)

            # 回溯，恢复现场
            board[i][j] = ch

        # 2. 从每个格子开始 DFS
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return ans