
class Solution:
    
    def dfs(self, node, adj, vis):
        
        vis[node] = True
        
        for nbr in adj[node]:
            if vis[nbr] == False:
                self.dfs(nbr, adj, vis)
                
    
    def topo(self, node, lis, vis, adj):
        
        vis[node] = True
        
        for nbr in adj[node]:
            if vis[nbr] == False:
                self.topo(nbr, lis, vis, adj)
            
        lis.append(node)
        
        
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        
        lis = []
        vis = [False for i in range(V)]
        
        for i in range(V):
            if vis[i] == False:
                self.topo(i, lis, vis, adj)
                
        adj2 = [[] for i in range(V)]
        
        for i in range(V):
            for node in adj[i]:
                adj2[node].append(i)
                
        vis = [False for i in range(V)]
        
        ans = 0
        
        for i in range(V-1, -1, -1):
            if vis[lis[i]] == False:
                ans += 1
                self.dfs(lis[i], adj2, vis)
                
        return ans
        
        
        
        