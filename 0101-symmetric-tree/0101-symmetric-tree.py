# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
     def isSymmetric(p, q):
        if not root:
            return True
        if not p or not q:
            return p == q
        return (p.val == q.val and isSymmetric(p.left, q.right) and isSymmetric(p.right, q.left))

     return isSymmetric(root, root)
        