
class Solution:
    
    def dfs(self, adj, dist, low, vis, timer, node, parent, ans):
        
        vis[node] = True
        
        dist[node] = timer
        low[node] = timer
        child = 0
        
        timer += 1
        
        for nbr in adj[node]:
            
            if nbr == parent:
                continue
            
            if vis[nbr] == False:
                
                self.dfs(adj, dist, low, vis, timer, nbr, node, ans)
                
                low[node] = min(low[node], low[nbr])
                
                if low[nbr] >= dist[node] and parent != -1:
                    ans.append(node)
                    
                child += 1
                    
            else:
                low[node] = min(low[node], dist[nbr])
        
        if parent == -1 and child > 1:
            ans.append(0)
    
    
    def biGraph(self, arr, V, e):
        # code here 
        if e == 1 and V == 2:
            return 1
        
        graph = [[] for i in range(V)]
        
        for i in range(0, 2*e, 2):
            
            u = arr[i]
            v = arr[i+1]
            
            graph[u].append(v)
            graph[v].append(u)
        
        dist = [-1]*V
        low = [-1]*V
        vis = [False]*V
        #v2 = [False]*V
        
        comp = 0
        
        ans = []
        
        timer = 0
        
        for i in range(V):
            if vis[i] == False:
                comp += 1
                if comp == 2:
                    return 0
                self.dfs(graph, dist, low, vis, timer, i, -1, ans)
        
        if len(ans) == 0:
            return 1
        
        return 0
        