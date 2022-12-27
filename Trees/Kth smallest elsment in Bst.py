
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    
    def inordertraversal(self, root, K):
        
        if root == None:
            return
        
        self.inordertraversal(root.left, K)
        
        if self.flag == 0:
            self.cnt += 1
            if self.cnt == K:
                self.ans = root.val
                self.flag = 1
                return
        else:
            return
        
        self.inordertraversal(root.right, K)
            
        
    
    def kthsmallest(self, A, B):
        
        self.ans = -1
        self.cnt = 0
        self.flag = 0
        
        self.inordertraversal(A, B)
        
        return self.ans
