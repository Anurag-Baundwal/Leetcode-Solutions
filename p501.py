class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.modes = []
        self.max_frequency = 0
        self.current_value = None
        self.current_frequency = 0
        
        def update_modes(val):
            if val != self.current_value:
                self.current_value = val
                self.current_frequency = 1
            else:
                self.current_frequency += 1
            
            if self.current_frequency == self.max_frequency:
                self.modes.append(self.current_value)
            elif self.current_frequency > self.max_frequency:
                self.modes = [self.current_value]
                self.max_frequency = self.current_frequency
        
        def in_order(node):
            if not node:
                return
            
            in_order(node.left)
            update_modes(node.val)
            in_order(node.right)
        
        in_order(root)
        return self.modes
        