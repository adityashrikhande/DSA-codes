
# rec + mem

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    
    def profit(self, A, idx, buy, trans, n, dp):
        
        if idx == n or trans == 0:
            return 0
        
        if dp[idx][buy][trans] != -1:
            return dp[idx][buy][trans]
        
        if buy:
            pro = max(-A[idx] + self.profit(A, idx+1, 0, trans, n, dp), self.profit(A, idx+1, 1, trans, n, dp))
        else:
            pro = max(A[idx] + self.profit(A, idx+1, 1, trans-1, n, dp), self.profit(A, idx+1, 0, trans, n, dp))
        
        dp[idx][buy][trans] = pro
        return dp[idx][buy][trans]
    
    def maxProfit(self, A):
        
        n = len(A)
        
        dp = [[[-1 for k in range(3)] for i in range(2)] for j in range(n)] 
        
        return self.profit(A, 0, 1, 2, n, dp)

# tabulation

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    
    def maxProfit(self, A):
        
        n = len(A)
        
        dp = [[[-1 for k in range(3)] for i in range(2)] for j in range(n+1)] 
        
        for idx in range(n, -1, -1):
            for buy in range(2):
                for trans in range(3):
                    
                    if idx == n or trans == 0:
                        dp[idx][buy][trans] = 0
                    else:
                        if buy:
                            pro = max(-A[idx] + dp[idx+1][0][trans] , dp[idx+1][1][trans])
                        else:
                            pro = max(A[idx] + dp[idx+1][1][trans-1], dp[idx+1][0][trans])

                        dp[idx][buy][trans] = pro
        
        
        return dp[0][1][2]


# space optimisation

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    
    def maxProfit(self, A):
        
        n = len(A)
        
        ahead = [[0 for k in range(3)] for i in range(2)] 
        cur = [[0 for k in range(3)] for i in range(2)] 
        
        for idx in range(n-1, -1, -1):
            for trans in range(1, 3):
                    
                cur[1][trans] = max(-A[idx] + ahead[0][trans] , ahead[1][trans])
                cur[0][trans] = max(A[idx] + ahead[1][trans-1], ahead[0][trans])

            ahead = cur
        
        return ahead[1][2]