# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag = False
        def sumNode(node, current_s):
            nonlocal flag
            if node is None:
                return
            current_s += node.val
            if node.left is None and node.right is None:
                if current_s == targetSum:
                    flag = True
                
                return
            sumNode(node.left, current_s)
            sumNode(node.right, current_s)
        
        sumNode(root, 0)
        
        return flag
    
        