
# leetcode critical connections in a network

class Solution(object):  
    
    def dfs(self, graph, timer, dist, low, vis, parent, node, result):
        
        vis[node] = True
        
        dist[node] = timer
        low[node] = timer
        
        timer += 1
        
        for nbr in graph[node]:
            
            if nbr == parent:
                continue
            
            if vis[nbr] == False:
                
                self.dfs(graph, timer, dist, low, vis, node, nbr, result)
                
                low[node] = min(low[node], low[nbr])
                
                if dist[node] < low[nbr]:
                    ans = [node, nbr]
                    result.append(ans)
                        
            else:
                low[node] = min(dist[nbr], low[node])
    
    
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = [[] for i in range(n)]
        
        for edg in connections:
            u = edg[0]
            v = edg[1]
            
            graph[u].append(v)
            graph[v].append(u)
            
        timer = 0
        dist = [-1]*n
        low = [-1]*n
        vis = [False]*n
        
        result = []
        
        self.dfs(graph, timer, dist, low, vis, -1, 0, result)
        
        return result
        