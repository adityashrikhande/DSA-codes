
# Recursion + memo

class Solution:
    
    dp = [[-1 for i in range(1000+1)] for j in range(1000+1)]
    
    def solve(self,wt, val, W, n):
        
        if n == 0 or W == 0:
            return 0
            
        if self.dp[n][W] != -1:
            return self.dp[n][W]
            
        if W < wt[n-1]:
            self.dp[n][W] = self.solve(wt, val, W, n-1)
            return self.dp[n][W]
           
        self.dp[n][W] = max(self.solve(wt, val, W-wt[n-1], n-1) + val[n-1], self.solve(wt, val, W, n-1))
        return self.dp[n][W]
        
        
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        
        for i in range(n+1):
            for j in range(W+1):
                self.dp[i][j] = -1
        
        return self.solve(wt, val, W, n)


# DP tabulation

class Solution:
    
    def knapSack(self, W, wt, val, n):
        
        dp = [[0 for i in range(W+1)] for j in range(n+1)]
        
        for i in range(n+1):
            for j in range(W+1):
                
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
                elif j >= wt[i-1]:
                    dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
                
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][W]
        