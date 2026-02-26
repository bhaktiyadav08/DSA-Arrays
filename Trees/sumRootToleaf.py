class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
            if not node:
                return 0
            
            # Update current path's binary value
            # Equivalent to (current_val * 2) + node.val
            current_val = (current_val << 1) | node.val
            
            # If it's a leaf, return the accumulated path value
            if not node.left and not node.right:
                return current_val
            
            # Recurse left and right, summing the results
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)
