
class Solution:
	# @param A : root node of tree
	# @return an integer
    flag = 1
    
    def checkheight(self, root):
        
        if root == None:
            return 0
        
        lheight = self.checkheight(root.left)
        
        if lheight == -1:
            return -1
               
        rheight = self.checkheight(root.right)
        
        if rheight == -1:
            return -1
            
        if abs(lheight - rheight) > 1:
            return -1
            
        return max(lheight, rheight) + 1
        
    
    def isBalanced(self, A):
        
        if self.checkheight(A) != -1:
            return 1
        else:
            return 0
        
        