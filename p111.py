class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
