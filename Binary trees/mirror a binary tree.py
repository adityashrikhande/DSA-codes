
class Solution:
    
    def solve(self, root):
        if root == None:
            return None
        
        left = self.solve(root.left)
        right= self.solve(root.right)
        
        root.left = right
        root.right = left
        
        return root
        
        
    
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        return self.solve(root)