# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def findDiameter(node):
            nonlocal max_len
            if node is None:
                return 0
            l = findDiameter(node.left)
            r = findDiameter(node.right)
            max_len = max(max_len, l + r)
            return 1 + max(l, r)
        
        findDiameter(root)
        return max_len

        