# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def choose(node):
            if node is None:
                return 0, 0
            y_left, n_left = choose(node.left)
            y_right, n_right = choose(node.right)
            choose_cur = n_left + node.val + n_right
            n_choose_cur = max(y_left, n_left) + max(y_right, n_right)
            return choose_cur, n_choose_cur
        return max(choose(root))
        
        