
from heapq import heapify, heappush, heappop

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        heap = []
        heapify(heap)
        
        heappush(heap, (0, S))
        
        dist = [1e9 for i in range(V)]
        
        dist[S] = 0
        
        while len(heap) != 0:
            
            top = heappop(heap)
            
            for node in adj[top[1]]:
                if top[0] + node[1] < dist[node[0]]:
                    dist[node[0]] = top[0] + node[1]
                    heappush(heap, (dist[node[0]], node[0]))
                    
        return dist
            
            