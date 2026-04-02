# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            if left == -1:          # 左子树已经不平衡了，直接传上去
                return -1
            right = dfs(node.right)
            if right == -1:         # 右子树已经不平衡了，直接传上去
                return -1
            if abs(left - right) > 1:  # 当前节点不平衡
                return -1
            return max(left, right) + 1  # 平衡的话正常返回高度

        return dfs(root) != -1 
            

        