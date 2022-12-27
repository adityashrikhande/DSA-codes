
class Solution(object):
    def rotate(self, matrix):       # Rotate by 90 degrees
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            l = 0
            r = n-1
            
            while l < r:
                matrix[i][l],matrix[i][r] = matrix[i][r],matrix[i][l]
                l += 1
                r -= 1

def rotateMatrix(mat, n, m):   # Rotate by 1 element clockwise
    
    if n > m:
        l = m
    else:
        l = n
    
    l = l//2

    # Write your code here
    for i in range(l):
        temp = mat[i][i]
        for j in range(i+1, n-i):
            mat[j-1][i] = mat[j][i]
        for j in range(i+1, m-i):
            mat[n-i-1][j-1] = mat[n-i-1][j]
        for j in range(n-i-2, i-1, -1):
            mat[j+1][m-i-1] = mat[j][m-i-1]
        for j in range(m-i-2, i, -1):
            mat[i][j+1] = mat[i][j]
        mat[i][i+1] = temp
            