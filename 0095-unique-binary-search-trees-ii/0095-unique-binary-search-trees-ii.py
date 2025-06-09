# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        
        def build_trees(start, end):
            trees = []

            if start > end:
                trees.append(None)
                return trees
            
            for i in range(start, end+1):
                left = build_trees(start, i-1)
                right = build_trees(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r 
                        trees.append(root)
            return trees

        return build_trees(1, n)
        