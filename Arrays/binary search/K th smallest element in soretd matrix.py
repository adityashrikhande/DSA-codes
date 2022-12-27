
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]
        
        while l < r:
            mid = (l+r)//2
            
            if self.mycount(mid,matrix,n) < k:
                l = mid + 1
            else:
                r = mid
        
        return r
    
    def mycount(self, i, matrix,n):
        row = 0
        col = n-1
        count = 0
        while row < n and col >= 0:
            if matrix[row][col] <= i:
                count += col + 1
                row += 1
            else:
                col -= 1
                
        return count