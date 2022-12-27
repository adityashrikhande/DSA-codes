
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        
        n = len(A[0])
        
        if n == 1:
            return max(A[1][0], A[0][0])
        
        dp = [0 for i in range(n)]
        
        dp[0] = max(A[1][0], A[0][0])
        dp[1] = max(dp[0], A[0][1], A[1][1])
        
        for i in range(2, n):
            
            dp[i] = max(max(A[0][i], A[1][i]) + dp[i-2], dp[i-1])
            
        return dp[n-1]
            
# space optimised O(1)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        
        n = len(A[0])
        
        if n == 1:
            return max(A[1][0], A[0][0])
        
        prev2 = max(A[1][0], A[0][0])
        prev1 = max(prev2, A[0][1], A[1][1])
        
        for i in range(2, n):
            
            cur = max(max(A[0][i], A[1][i]) + prev2, prev1)
            
            prev2 = prev1
            prev1 = cur
            
        return prev1