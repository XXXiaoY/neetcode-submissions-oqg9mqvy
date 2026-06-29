# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        def dfs(node, layer):
            if node is None:
                return
            
            if len(ans) == layer:
                ans.append(node.val)
            
            dfs(node.right, layer + 1)
            dfs(node.left, layer + 1)
        
        dfs(root, 0)
        return ans
            
        