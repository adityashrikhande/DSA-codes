
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        
        root = A
        
        if root == None:
            return 0
        
        l = 1 + self.maxDepth(root.left) 
        
        r = 1 + self.maxDepth(root.right)
            
        return max(l,r)   