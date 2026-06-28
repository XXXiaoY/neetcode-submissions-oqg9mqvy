"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        if node is None:
            return
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
                
            new = Node(node.val)
            oldToNew[node] = new
            for i in node.neighbors:
                new.neighbors.append(dfs(i))
            return new
        
        return dfs(node)
            
        