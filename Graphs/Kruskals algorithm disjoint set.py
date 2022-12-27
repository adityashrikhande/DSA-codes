
class Solution:
    
    def makeset(self, parent, rank, V):
        for i in range(V):
            parent[i] = i
            rank[i] = 0
            
    def findparent(self, parent, node):
        
        if parent[node] == node:
            return node
            
        parent[node] = self.findparent(parent, parent[node])
        return parent[node]
            
    def union(self, parent, rank, u, v):
        
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[v] < rank[u]:
            parent[v] = u
        else:
            parent[u] = v
            rank[v] += 1
        
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        parent = [0]*V
        rank = [0]*V
        
        self.makeset(parent, rank, V)
        #code here
        
        lis = []
        
        for i in range(V):
            for edg in adj[i]:
                lis.append((edg[1], i, edg[0]))
                
        lis.sort()
        
        n = len(lis)
        
        ans = 0
        
        for i in range(n):
            
            u = self.findparent(parent, lis[i][1])
            v = self.findparent(parent, lis[i][2])
            wt = lis[i][0]
            
            if u != v:
                ans += wt
                self.union(parent, rank, u, v)
                
            
        return ans    
            
            