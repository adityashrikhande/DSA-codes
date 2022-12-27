
class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    
    def BST(self, i, j, A):
        
        if j < i:
            return None
        
        mid = (i + j)//2
        
        root = TreeNode(A[mid])  # inbuild function to create a node
        
        root.left = self.BST(i, mid-1, A)
        root.right = self.BST(mid+1, j, A)
        
        return root
    
    def sortedArrayToBST(self, A):
        
        n = len(A)
        
        return self.BST(0, n-1, A)
        
        