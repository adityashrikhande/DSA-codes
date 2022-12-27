
# rec + mem 

dp = [[-1 for i in range(5005)] for j in range(305)]

class Solution(object): #leetcode
    
    def CoinChange(self, a, i, summ, add):
        
        if i == len(a):
            return 0
            
        if dp[i][add] != -1:
            return dp[i][add]
            
        if summ == add:
            dp[i][add] = 1
            return dp[i][add]
            
        if a[i] > summ-add:
            dp[i][add] = self.CoinChange(a, i+1, summ, add)
            return dp[i][add]
            
        dp[i][add] = self.CoinChange(a, i, summ, add + a[i]) + self.CoinChange(a, i+1, summ, add)
        
        return dp[i][add]
    
    
    def change(self, n, a):
        # code here 
        
        if n == 0:
            return 1
        
        global dp
        
        #dp = [[-1 for i in range(5005)] for j in range(305)]
        
        m = len(a)
        
        for i in range(m+1):
            for j in range(n+1):
                dp[i][j] = -1
            
        return self.CoinChange(a, 0, n, 0)
        
# DP tebulation  time O(N*M),  space O(N)

class Solution:
    
    def count(self, S, m, n):
        # code here 
        
        if n == 0:
            return 1
            
        prev = [0 for i in range(n+1)]
        dp = [0 for i in range(n+1)]
        
        for i in range(1, m+1):
            for j in range(n+1):
                
                if i == 0:
                    dp[j] = 0
                elif j == 0:
                    dp[j] = 1
                
                elif j < S[i-1]:
                    dp[j] = prev[j]
                
                else:
                    dp[j] = prev[j] + dp[j-S[i-1]]
                    
            prev = dp
                    
        return dp[n]
                    
        