# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checksame(node1, node2):
            if node1 is None or node2 is None:
                return node1 == node2
            return node1.val == node2.val and checksame(node1.right, node2.right) and checksame(node1.left, node2.left)
        

        ans = False
        


        def dfs(node):
            if node is None:
                return
            nonlocal ans
            if node.val == subRoot.val:
                ans = ans or checksame(node,subRoot)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ans

        