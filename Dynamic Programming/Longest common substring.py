
# DP Tabulation

dp = [[-1 for i in range(1001)] for j in range(1001)]

def LCS(s1, s2, i, j):
    
    maxi = 0
        
    for i in range(i+1):
        for j in range(j+1):
            
            if i == 0 or j == 0:
                dp[i][j] = 0
                
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxi = max(maxi, dp[i][j])            # max will not get at last dp[n][m]
            
            else:
                dp[i][j] = 0                            
                
    return maxi                                         # max will not get at last dp[n][m]


class Solution(object):
    
    def longestCommonSubstr(self, s1, s2, n, m):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        for i in range(n+1):
            for j in range(m+1):
                dp[i][j] = -1
                     
        
        return LCS(s1, s2, n, m)

        
        # code here
