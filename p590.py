"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        """
        Returns the postorder traversal of the nodes' values of the given n-ary tree.

        Args:
            root: The root of the n-ary tree.

        Returns:
            A list of the nodes' values in postorder order.
        """
        if root is None:
            return []

        postorder_values = []
        for child in root.children:
            postorder_values += self.postorder(child)

        postorder_values.append(root.val)

        return postorder_values