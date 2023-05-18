# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0
        self.treeSum(root)
        return self.total_tilt

    # for calculating the sum of all subtree values
    def treeSum(self, root):
        if root is None:
            return 0
        left_sum = self.treeSum(root.left)
        right_sum = self.treeSum(root.right)
        tilt = abs(left_sum - right_sum)
        self.total_tilt += tilt
        return root.val + left_sum + right_sum
