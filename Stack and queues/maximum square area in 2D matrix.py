
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        
        m = len(matrix)
        A = []
        n = len(matrix[0])
        ans = 0
          
        for i in range(n):
            if matrix[0][i] == "1":
                A.append(1)
                ans = 1
            else:
                A.append(0)
                
        parr = [0]*n
                
        for i in range(m):
            for j in range(n):
                
                if j == 0:
                    if matrix[i][j] == "1":
                        A[j] = 1
                    else:
                        A[j] = 0
                        
                    ans = max(ans, A[j])
                
                else:
                    if matrix[i][j] == "1":
                    
                        A[j] = 1 + min({parr[j], parr[j-1], A[j-1]})
                        ans = max(ans,A[j])
                    else:
                        
                        A[j] = 0
            
            parr = A.copy()
            
        return ans*ans            
            