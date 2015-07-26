# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    '''
    lis will contains integers to be printed
    n is level of node printed
    n1 is level returned backwards
    '''
    def show(self,root,lis, n, n_covered):
        if root:
            if n_covered < n:
                lis.append(root.val)
                n_covered += 1
            n_covered = self.show(root.right,lis,n+1, n_covered)
            n_covered = self.show(root.left,lis,n+1, n_covered)
        return n_covered
        
        
    def rightSideView(self, root):
        lis = []
        self.show(root,lis,0,-1)
        return lis
