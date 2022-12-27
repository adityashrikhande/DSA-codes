
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    
    def PathSum(self, root, Sum, pathlist, cursum):
        
        if root.left == None and root.right == None:
            if Sum == cursum + root.val:
                self.ans.append(pathlist + [root.val])
            return
                
        if root.left != None: 
            self.PathSum(root.left, Sum, pathlist + [root.val], cursum + root.val)
            
        if root.right != None:        
            self.PathSum(root.right, Sum, pathlist + [root.val], cursum + root.val)
    
    def pathSum(self, A, B):
        
        pathlist = []
        
        self.ans = [] # class variable
        
        self.PathSum(A, B, pathlist, 0)
        
        return self.ans