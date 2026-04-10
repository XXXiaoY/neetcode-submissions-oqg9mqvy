# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        def isSameTree(p1, p2):
            if p1 is None or p2 is None:
                return p1 == p2
            return p1.val == p2.val and isSameTree(p1.left, p2.left) and isSameTree(p1.right, p2.right)
        
        def check(node):
            if node is None:
                return
            nonlocal ans
            if node.val == subRoot.val:
                ans = ans or isSameTree(node, subRoot)
            check(node.right)
            check(node.left)

        check(root)
        
        return ans
        