# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, max_v):
            nonlocal cnt
            if node is None:
                return
            if node.val >= max_v:
                cnt += 1
            max_v = max(max_v, node.val)

            dfs(node.left, max_v)
            dfs(node.right, max_v)
        dfs(root, float('-inf'))
        
        return cnt
        