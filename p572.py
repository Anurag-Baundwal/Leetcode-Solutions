class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "null"
            return f"#{node.val} {serialize(node.left)} {serialize(node.right)}"
        
        root_serialized = serialize(root)
        subroot_serialized = serialize(subRoot)
        print (root_serialized)
        print (subroot_serialized)

        return subroot_serialized in root_serialized