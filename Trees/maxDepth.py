class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
       self.val=val
       self.left=left
       self.right=right
class solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return 1 + max(left_depth,right_depth)
root = TreeNode(3)                    # Level 1: 3
root.left = TreeNode(9)               # Level 2 left: 9
root.right = TreeNode(20)             # Level 2 right: 20
root.right.left = TreeNode(15)  
root.right.right = TreeNode(7)  
solution = solution()
print("Tree depth:", solution.maxDepth(root)) 