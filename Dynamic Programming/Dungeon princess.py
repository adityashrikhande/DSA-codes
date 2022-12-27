
# dp solution

class Solution(object):
    
    def calculateMinimumHP(self, A):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        
        dp = [[1e9 for i in range(n+1)] for j in range(m+1)]
        
        dp[m][n] = 1
        dp[m-1][n] = 1
        dp[m][n-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                minpower = min(dp[i+1][j], dp[i][j+1]) - A[i][j]
                
                if minpower <= 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = minpower
                    
        return dp[0][0]

# Rec + mem

class Solution(object):
    
    def minpts(self, A, i, j, dp):
        
        if i == len(A)-1 and j == len(A[0])-1:
            if A[i][j] > 0:
                return 1
            else:
                return -A[i][j] + 1
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        if i + 1 == len(A):
            dp[i][j] = max(1, self.minpts(A, i, j+1, dp) - A[i][j])
            return dp[i][j]    
        
        if j + 1 == len(A[0]):
            dp[i][j] = max(1, self.minpts(A, i+1, j, dp) - A[i][j])   
            return dp[i][j]     
                  
        dp[i][j] = max(1, min(self.minpts(A, i+1, j, dp)-A[i][j], self.minpts(A, i, j+1, dp)-A[i][j]))
        return dp[i][j]    
    
    def calculateMinimumHP(self, A):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        return self.minpts(A, 0, 0, dp)
        