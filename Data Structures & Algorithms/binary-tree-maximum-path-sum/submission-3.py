# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ans = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal max_ans
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # 1. 更新全局最大值：当前节点作为“最高转折点”的路径
            # 路径为：左子树贡献 + 右子树贡献 + 当前节点值
            max_ans = max(max_ans, node.val + left_gain + right_gain)
            
            # 2. 返回给父节点：当前节点能提供的“单边”最大贡献
            # 必须从左、右中选一个最大的，加上自己
            return node.val + max(left_gain, right_gain)
        
        dfs(root)

        return max_ans
        