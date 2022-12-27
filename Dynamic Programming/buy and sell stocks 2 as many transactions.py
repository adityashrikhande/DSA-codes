
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
            
            if A[i]-mini > 0:
                maxprofit += A[i]-mini
                mini = A[i]
            
            mini = min(mini, A[i])
            
        return maxprofit

# rec + mem

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    
    def profit(self, A, idx, buy, n, dp):
        
        if idx == n:
            return 0
        
        if dp[idx][buy] != -1:
            return dp[idx][buy]
        
        if buy:
            pro = max(-A[idx] + self.profit(A, idx+1, 0, n, dp), self.profit(A, idx+1, 1, n, dp))
        else:
            pro = max(A[idx] + self.profit(A, idx+1, 1, n, dp), self.profit(A, idx+1, 0, n, dp))
        
        dp[idx][buy] = pro
        return dp[idx][buy]
    
    def maxProfit(self, A):
        
        n = len(A)
        
        dp = [[-1 for i in range(2)] for j in range(n)]
        
        return self.profit(A, 0, 1, n, dp)

# dp tabulation 

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    
    def maxProfit(self, A):
        
        n = len(A)
        
        dp = [[-1 for i in range(2)] for j in range(n+1)]
        
        for idx in range(n, -1, -1):
            for buy in range(2):
                
                if idx == n:
                    dp[idx][buy] = 0
                else:
                    if buy:
                        pro = max(-A[idx] + dp[idx+1][0] , dp[idx+1][1])
                    else:
                        pro = max(A[idx] + dp[idx+1][1], dp[idx+1][0])

                    dp[idx][buy] = pro
                
        return dp[0][1]

# space optimisation O(1)

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    
    def maxProfit(self, A):
        
        n = len(A)
        
        aheadbuy = 0
        aheadnotbuy = 0
        
        for idx in range(n-1, -1, -1):    
                    
            curbuy = max(-A[idx] + aheadnotbuy , aheadbuy)
            curnotbuy = max(A[idx] + aheadbuy, aheadnotbuy)

            aheadbuy = curbuy
            aheadnotbuy = curnotbuy

        return aheadbuy
    