"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        clone = {}  

        def dfs(current):
            if current in clone:
                return clone[current]
            
            copy = Node(current.val)
            clone[current] = copy       

            for neighbor in current.neighbors: 
                copy.neighbors.append(dfs(neighbor))  

            return copy
        
        return dfs(node)
