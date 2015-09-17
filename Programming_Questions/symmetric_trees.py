# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def ismirror(self, x, y):
        if x is None and y is None:
            return True
        elif x is None or y is None:
            return False
        elif x.val != y.val:
            return False
        else:
            return  self.ismirror(x.right, y.left) and self.ismirror(x.left, y.right)
        
    def isSymmetric(self, root):
        if root:
            return self.ismirror(root.left, root.right)
        else:
            return True
        """
        :type root: TreeNode
        :rtype: bool
        """
        
