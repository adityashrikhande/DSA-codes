
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        
        n = len(A)
        
        ma = A[0]
        mi = A[0]
        ans = A[0]
        
        for i in range(1, n):
            
            if A[i] < 0:
                ma,mi = mi, ma
            
            ma = max(A[i], ma*A[i])
            mi = min(A[i], mi*A[i])
            
            ans = max(ans, ma)
        
        return ans 


# Another similar approach

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        
        n = len(A)
        
        ma = 1
        mi = 1
        ans = A[0]
        
        for i in range(n):
            
            temp = A[i]*ma
            
            ma = max(A[i]*mi, A[i]*ma, A[i])
            mi = min(A[i]*mi, temp, A[i])
            
            ans = max(ans, ma)
        
        return ans    
                    
            
        
        
        
        
           
                    
            
        
        
        
        
        