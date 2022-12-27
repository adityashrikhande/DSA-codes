
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    
    def min_operations(self, A, B, sta, stb, dp):
            
        if sta < 0:
            return stb+1
            
        if stb < 0:
            return sta+1
            
        if dp[sta][stb] != -1:
            return dp[sta][stb]
            
        if A[sta] == B[stb]:
            dp[sta][stb] = self.min_operations(A, B, sta-1, stb-1, dp)
            return dp[sta][stb]
            
        dp[sta][stb] = 1 + min(self.min_operations(A, B, sta-1, stb, dp), min(self.min_operations(A, B, sta, stb-1, dp), self.min_operations(A, B, sta-1, stb-1, dp)))
        return dp[sta][stb]

    def minDistance(self, A, B):
        
        a = len(A)
        b = len(B)
        
        dp = [[-1 for i in range(451)] for j in range(451)]
        
        return self.min_operations(A, B, a-1, b-1, dp)


# Tabulation

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def minDistance(self, A, B):
        
        a = len(A)
        b = len(B)
        
        dp = [[-1 for i in range(b+1)] for j in range(a+1)]
        
        for i in range(a+1):
            dp[i][0] = i
        
        for j in range(b+1):
            dp[0][j] = j
        
        for i in range(1, a+1):
            for j in range(1, b+1):
                
                if A[i-1] == B[j-1]:                    
                    dp[i][j] = dp[i-1][j-1]
                else:                   
                    dp[i][j] = 1 + min({dp[i-1][j-1], dp[i][j-1], dp[i-1][j]})
                    
        return dp[a][b]

# Tabulation O(N) space

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def minDistance(self, A, B):
        
        a = len(A)
        b = len(B)
        
        dp = [i for i in range(b+1)]
        prev = dp[:]
        
        for i in range(1, a+1):
            for j in range(0, b+1):
                
                dp[0] = i
                
                if A[i-1] == B[j-1]:                   
                    dp[j] = prev[j-1]
                else:                 
                    dp[j] = 1 + min({prev[j-1], dp[j-1], prev[j]})
                    
            prev = dp[:]
                    
        return dp[b]