
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        
        n = len(A)
        
        if n <= 1:
            return 0
        
        mini = A[0]
        maxprofit = 0
        
        for i in range(1, n):
            
            maxprofit = max(maxprofit, A[i]-mini)
            
            mini = min(A[i], mini)
            
        return maxprofit
            