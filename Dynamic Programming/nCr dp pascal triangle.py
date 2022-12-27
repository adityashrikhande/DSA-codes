
class Solution:                   # O(n*r)
    
    def nCr(self, n, r):
        # code here
        
        if n < r:
            return 0
            
        if n == r:
            return 1
        
        if n-r < r:
            r = n-r
        
        if r == 1:
            return n
        
        dp = [0 for i in range(r+1)]
        
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(r,0,-1):
                
                dp[j] += dp[j-1]%(1e9+7)

                
        return int(dp[r]%(1e9+7))
