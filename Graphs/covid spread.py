
class Solution:
    def helpaterp(self, hospital):
        # code here
        
        r = len(hospital)
        c = len(hospital[0])
        
        vis = [[False for i in range(c)] for j in range(r)]
        
        q1 = []
        q2 = []
        
        for i in range(r):
            for j in range(c):
                if hospital[i][j] == 2:
                    q1.append((i, j))
                    vis[i][j] = True
                    
        timer = 0
        
        while len(q1) != 0:
            
            temp = q1.pop()
            i = temp[0]
            j = temp[1]
            
            if i-1 != -1 and vis[i-1][j] == False:
                if hospital[i-1][j] == 1:
                    vis[i-1][j] = True
                    q2.append((i-1, j))
                     
            if i+1 != r and vis[i+1][j] == False:
                if hospital[i+1][j] == 1:
                    vis[i+1][j] = True
                    q2.append((i+1, j))
                
            if j-1 != -1 and vis[i][j-1] == False:    
                if hospital[i][j-1] == 1:
                    vis[i][j-1] = True
                    q2.append((i, j-1))
                
            if j+1 != c and vis[i][j+1] == False:
                if hospital[i][j+1] == 1:
                    vis[i][j+1] = True
                    q2.append((i, j+1))
            
            
            if len(q1) == 0:
                if len(q2) == 0:
                    break
                timer += 1
                q1 = q2[:]
                q2 = []
            
        for i in range(r):
            for j in range(c):
                if hospital[i][j] == 1 and vis[i][j] == False:
                    return -1
                    
        return timer
                
            