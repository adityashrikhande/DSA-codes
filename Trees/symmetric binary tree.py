
# Recursive approach

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def helperfunction(self, left, right):
        
        if left == None or right == None:
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.helperfunction(left.left, right.right) and self.helperfunction(left.right, right.left)
        
        
    
    def isSymmetric(self, A):
        
        if A == None:
            return True
        
        return self.helperfunction(A.left, A.right)


# Iterative approach

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def isSymmetric(self, A):
        
        if A == None:
            return 1
        
        q = [A.left, A.right]
        
        while len(q) != 0:
            
            left = q.pop(0)
            right = q.pop(0)
            
            if left == None and right == None:
                continue
            
            if (left == None and right != None) or (left != None and right == None):
                return False
            
            if left.val != right.val:
                return False
            
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
              
        
        return True



            
        