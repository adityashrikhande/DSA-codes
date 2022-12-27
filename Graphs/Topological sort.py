
# DFS

class Solution:
    
    def dfs(self, adj, node, vis, st):
        
        vis[node] = 1
        
        for i in adj[node]:
            
            if vis[i] == 0:
                
                self.dfs(adj, i, vis, st)
                
        st.append(node)
                
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        vis = [0 for i in range(V)] 
        st = []
        
        for i in range(V):
            if vis[i] == 0:
                self.dfs(adj, i, vis, st)
                
        n = len(st)
        l = 0
        r = n-1
        
        while l < r:
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1
            
        return st


# BFS  indegree method

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        indegree = [0 for i in range(V)]
        
        q = []
        
        for li in adj:
            for node in li:
                indegree[node] += 1
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        
        while len(q) != 0:
            
            node = q[0]
            q.pop(0)
            topo.append(node)
            
            for i in adj[node]:
                
                indegree[i] -= 1
                
                if indegree[i] == 0:
                    q.append(i)
                    
        return topo    
                    
