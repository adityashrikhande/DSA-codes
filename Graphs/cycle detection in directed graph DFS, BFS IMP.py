
# DFS

class Solution:
    
    def detectcycle(self, node, adj, vis, dfsvis):
           
        vis[node] = 1
        dfsvis[node] = 1
        
        for i in adj[node]:
            
            if vis[i] == 1:
                if dfsvis[i] == 1:
                    return True
            else:
                if self.detectcycle(i, adj, vis, dfsvis):
                    return True
                
            
        dfsvis[node] = 0
                
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        dfsvis = [0]*V
        vis = [0]*V
        
        for i in range(V):
            
            if vis[i] == 0:
                if self.detectcycle(i, adj, vis, dfsvis):
                    return True
               
        return False

# BFS    Kahn's algorithm

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        q = []
        
        indeg = [0 for i in range(V)]
        
        for li in adj:
            for node in li:
                indeg[node] += 1
                
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
                
        cnt = 0
        
        while len(q) != 0:
            
            node = q[0]
            q.pop(0)
            cnt += 1
            
            for i in adj[node]:
                indeg[i] -= 1
                
                if indeg[i] == 0:
                    q.append(i)
                    
        if cnt == V:
            return False
        
        return True
        
        