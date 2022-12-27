
# rec + mem

mod = 1e9 + 7

class Solution:
    # @param A : string
    # @return an integer
    
    def ways(self, A, end, dp):
        
        if end < 0:
            return 1
            
        if dp[end] != -1:
            return dp[end]
        
        if int(end-1 != -1 and A[end] == '0'):
            dp[end] = int(self.ways(A, end-2, dp)%mod)
            return dp[end] 
        
        
        if (end-1 == -1) or A[end-1] == '0' or (10*int(A[end-1])+int(A[end]) < 10 or (10*int(A[end-1])+int(A[end])) > 26):
            dp[end] = int(self.ways(A, end-1, dp))
            return dp[end]
            
        dp[end] = int((self.ways(A, end-1, dp) + self.ways(A, end-2, dp)))
        return dp[end]
    
    def numDecodings(self, A):
        
        n = len(A)
        
        if A[0] == '0':
            return 0
        
        for i in range(1, n):
            if (A[i] == '0' and int(A[i-1]) >= 3) or (A[i] == '0' and int(A[i-1]) == 0):
                return 0
        
        dp = [-1 for i in range(n+1)]
        
        return int(self.ways(A, n-1, dp)%mod)


# Tabulation O(N) time space O(N)

mod = 1e9 + 7

class Solution:
    # @param A : string
    # @return an integer
    
    def numDecodings(self, A):
        
        n = len(A)
        
        if A[0] == '0':
            return 0
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        
        for i in range(1, n):
            if (A[i] == '0' and int(A[i-1]) >= 3) or (A[i] == '0' and int(A[i-1]) == 0):
                return 0
                
        dp[1] = 1
                
        for i in range(2, n+1):
            if int(A[i-2:i]) < 10 or int(A[i-2:i]) > 26:
                dp[i] = dp[i-1]
            elif int(A[i-2:i]) == 10:
                dp[i] = dp[i-2]
            else:
                dp[i] = (dp[i-1] + dp[i-2])%mod
    
        return int(dp[n]%mod)