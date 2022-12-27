
# Rec + Memo

dp = [[-1 for i in range(1001)] for j in range(1001)]

def LCS(s1, s2, l1, l2):
        
    if l1 < 0 or l2 < 0:
        return 0
    
    if dp[l1][l2] != -1:
        return dp[l1][l2]

    if s1[l1] == s2[l2]:
        dp[l1][l2] = 1 + LCS(s1, s2, l1-1, l2-1)
        return dp[l1][l2]

    dp[l1][l2] = max(LCS(s1, s2, l1-1, l2), LCS(s1, s2, l1, l2-1))
    
    return dp[l1][l2]


class Solution(object):
    
    def longestCommonSubsequence(self, s1, s2):
        
        l1 = len(s1)
        l2 = len(s2)
        
        for i in range(l1+1):
            for j in range(l2+1):
                dp[i][j] = -1
                     
        
        return LCS(s1,s2, l1-1, l2-1)


# DP tabulation   O(N*N) both

dp = [[-1 for i in range(1001)] for j in range(1001)]

def LCS(s1, s2, i, j):
        
    for i in range(i+1):
        for j in range(j+1):
            
            if i == 0 or j == 0:
                dp[i][j] = 0
                
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[i][j]
        


class Solution(object):
    
    def longestCommonSubsequence(self, s1, s2):
        
        l1 = len(s1)
        l2 = len(s2)
        
        for i in range(l1+1):
            for j in range(l2+1):
                dp[i][j] = -1
                     
        
        return LCS(s1, s2, l1, l2)