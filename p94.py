# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursively
    def inorderTraversal(self, root):
        res = []
        self.dfs_inorder(root, res)
        return res
    
    def dfs_inorder(self, root, res):
        if root:
            self.dfs_inorder(root.left, res)
            res.append(root.val)
            self.dfs_inorder(root.right, res)