# BFS
class Solution:
    
    def detectcycle(self, node, adj, parent, vis):
        
        q = []
        q.append((node, parent))
        
        while len(q) != 0:
            
            m = q.pop(0)
            nod = m[0]
            par = m[1]
            vis[nod] = 1
            
            for i in adj[nod]:
                if vis[i] == 0:
                    vis[i] = 1
                    q.append((i, nod))
                else:
                    if i != par:
                        return True
            
        return False    
    
    #Function to detect cycle in an undirected graph.
    
    def isCycle(self, V, adj):
		#Code here
		
		prev = -1
		n = len(adj)
		vis = [0]*n
		
		for i in range(n):
		    
		    if vis[i] == 0:
		        if self.detectcycle(i, adj, -1, vis):
		            return True
		    
		return False

# DFS

class Solution:
    
    def detectcycle(self, node, adj, parent, vis):
        
        vis[node] = 1
        
        for nod in adj[node]:
            
            if vis[nod] == 0:
                if self.detectcycle(nod, adj, node, vis):
                    return True
            else:
                if nod != parent:
                    return True
            
        return False    
    
    #Function to detect cycle in an undirected graph.
    
    def isCycle(self, V, adj):
		#Code here
		
		prev = -1
		n = len(adj)
		vis = [0]*n
		
		for i in range(n):
		    
		    if vis[i] == 0:
		        if self.detectcycle(i, adj, -1, vis):
		            return True
		    
		return False
		    
		    
		
		
		    
		
		