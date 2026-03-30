"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 记录 原节点 -> 新节点 的映射
        visited = {}

        def dfs(curr):
            if not curr:
                return None
            
            # 如果这个节点已经克隆过了，直接返回克隆后的那个
            if curr in visited:
                return visited[curr]

            # 1. 克隆当前节点（只克隆值，不克隆邻居）
            clone_node = Node(curr.val, [])
            # 2. 存入哈希表，防止死循环
            visited[curr] = clone_node

            # 3. 递归处理邻居
            for neighbor in curr.neighbors:
                # 递归克隆邻居，并把它加到新节点的邻居列表里
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node

        return dfs(node)
 
        
        
        