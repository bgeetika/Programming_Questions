# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.lis = []
        while root:
            self.lis.append(root)
            root = root.left
        
        
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.lis:
            return True
        else:
            return False
        

    # @return an integer, the next smallest number
    def next(self):
        x =  self.lis.pop()
        curr = x.right
        while(curr):
            self.lis.append(curr)
            curr = curr.left
        return x.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
