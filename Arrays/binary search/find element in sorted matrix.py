
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        lo = 0
        hi = m*n - 1
        
        while lo <= hi:
            
            mid = lo + (hi-lo)//2
            
            if matrix[mid//n][mid%n] < target:
                lo = mid + 1
            elif matrix[mid//n][mid%n] > target:
                hi = mid - 1
            else:
                return True
            
        return False

# 2 nd approach

def findTargetInMatrix(mat, m, n, target):
	# Write your code here.
    i = 0
    j = n-1
    for k in range(m+n):
        if mat[i][j] > target:
            j -= 1
            if j == -1:
                break
        elif mat[i][j] < target:
            i += 1
            if i == m:
                break
        else:
            return 1
        
    return 0
        