# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0
            
            left_height = check(node.left)
            if left_height == -1:
                return -1
            
            right_height = check(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
        
            return 1 + max(left_height, right_height)
    
        return check(root) != -1
