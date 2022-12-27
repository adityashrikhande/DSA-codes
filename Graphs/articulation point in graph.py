
import sys
sys.setrecursionlimit(10**6)

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
        
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        
        dist = [-1]*V
        low = [-1]*V
        vis = [False]*V
        
        ans = []
        
        timer = 0
        
        self.dfs(adj, dist, low, vis, timer, 0, -1, ans)
        
        s = set(ans)
        
        ans = list(s)
        
        ans.sort()
        
        if len(ans) == 0:
            return [-1]
        
        return ans
        
        
        