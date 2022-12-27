
class Solution:
    
    def marea(self, i, j, n, m, grid, vis):
        
        if i == n or j == m or i == -1 or j == -1:
            return 0
            
        if vis[i][j] == True or grid[i][j] == 0:
            return 0
        
        vis[i][j] = True
        
        
        return 1 + (self.marea(i+1,j, n, m, grid, vis)+self.marea(i+1,j+1, n, m, grid, vis)+
        self.marea(i+1,j-1, n, m, grid, vis)+self.marea(i,j-1, n, m, grid, vis)
        +self.marea(i,j+1, n, m, grid, vis)+self.marea(i-1,j-1, n, m, grid, vis)+
        self.marea(i-1,j, n, m, grid, vis) + self.marea(i-1,j+1, n, m, grid, vis))
            

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		#Code here
		
		n = len(grid)
		m = len(grid[0])
		
		area = 0
		
		vis = [[False for i in range(m)] for j in range(n)]
		
		for i in range(n):
		    for j in range(m):
		        if grid[i][j] == 1 and vis[i][j] == False:
		            
		            area = max(area, self.marea(i, j, n, m, grid, vis))
		            
		return area
		            