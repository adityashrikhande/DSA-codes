
# prims algo Brute force more than O(N^2) comp time

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        mst = [False for i in range(V)]
        
        parent = [-1 for i in range(V)]
        
        key = [1e9 for i in range(V)]
        
        key[0] = 0
        
        for i in range(V-1):
            
            mini = 1e9
            
            for j in range(V):
                if mst[j] == False and key[j] < mini:
                    mini = key[j]
                    u = j
                    
            mst[u] = True
            
            for node in adj[u]:
                
                nd = node[0]
                wt = node[1]
                
                if mst[nd] != True and wt < key[nd]:
                    key[nd] = wt
                    parent[nd] = u
                    
        sum = 0
        for i in range(V):
            sum += key[i]
            
        return sum

            
            
        