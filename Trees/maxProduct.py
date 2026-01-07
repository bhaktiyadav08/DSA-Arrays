class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
       self.val=val
       self.left=left
       self.right=right
class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        # Step 1: Get total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        TOTAL = totalSum(root)
        self.maxProd = 0
        # Step 2: DFS to compute subtree sums & products
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = node.val + left + right
            self.maxProd = max(self.maxProd, s * (TOTAL - s))
            return s
        dfs(root)
        return self.maxProd % MOD
root = TreeNode(3)                    # Level 1: 3
root.left = TreeNode(9)               # Level 2 left: 9
root.right = TreeNode(20)             # Level 2 right: 20
root.right.left = TreeNode(15)  
root.right.right = TreeNode(7)  
solution = Solution()
print("Tree depth:", solution.maxProduct(root))