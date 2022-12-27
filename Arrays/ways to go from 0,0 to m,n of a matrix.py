
# REC + MEM

def paths(i, j, m, n, dp):
    if i == m-1 and j == n-1:
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if i + 1 == m:
        dp[i][j] = paths(i, j+1, m, n, dp)
        return dp[i][j]
    if j + 1 == n:
        dp[i][j] = paths(i+1, j, m, n, dp)
        return dp[i][j]
    dp[i][j] = paths(i+1, j, m, n, dp) + paths(i, j+1, m, n, dp)
    return dp[i][j]

def uniquePaths(m, n):
	# Write your code here.
    dp = [[-1 for i in range(n)] for j in range(m)]
	
    return paths(0, 0, m, n, dp)


# Tabulation

def uniquePaths(m, n):
	# Write your code here.
    dp = [[0 for i in range(n)] for j in range(m)]
	
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 or j == n-1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
    
    return dp[0][0]

# Space optimisation

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cur = [0 for i in range(n)]
        nex = [1 for i in range(n)]

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if j == n-1:
                    cur[j] = 1
                else:
                    cur[j] = nex[j] + cur[j+1]
            nex = cur

        return nex[0]
            
            