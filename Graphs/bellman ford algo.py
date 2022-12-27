
# Getting array of shortest distances

def bellman_ford(self, V, adj, S):
        #code here
        
        dist = [int(1e8) for i in range(V)]
        dist[S] = 0
        
        for i in range(V-1):
            
            for edg in adj:   # adj is list of edges
                
                u = edg[0]
                v = edg[1]
                wt = edg[2]
                
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                        
        return dist
                    
# Detecting if there is a -ve cycle

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		
		dist = [1e9 for i in range(n)]
		
		dist[0] = 0
		
		for i in range(n-1):
		
    		for edg in edges:
    		    u = edg[0]
    		    v = edg[1]
    		    wt = edg[2]
    		    
    		    if dist[u] + wt < dist[v]:
    		        dist[v] = dist[u] + wt
    		        
    	for edg in edges:
    		    u = edg[0]
    		    v = edg[1]
    		    wt = edg[2]
    		    
    		    if dist[u] + wt < dist[v]:
    		        
    		        return 1
    	
    	return 0
		    