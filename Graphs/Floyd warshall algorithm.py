
class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n = len(matrix)
		
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            
		            if matrix[i][k] != -1 and matrix[k][j] != -1:
		                if matrix[i][j] == -1:
		                    matrix[i][j] = matrix[i][k]+matrix[k][j]
		            	else:
		                    matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
        
        