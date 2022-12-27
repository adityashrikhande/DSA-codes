
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, graph):
        # code here
        
        ans = []
        vis = [0 for i in range(V)]
        
        q = [0]
        while len(q) != 0:
            parent = q.pop(0)
            if vis[parent] == 0:
                ans.append(parent)
            vis[parent] = 1
            for node in graph[parent]:
                if vis[node] != 1:
                    q.append(node)
                
        return ans
