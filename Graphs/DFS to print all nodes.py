
def dfs(graph, parent, vis, ans):
    vis[parent] = 1
    ans.append(parent)
    for node in graph[parent]:
        if vis[node] == 0:
            dfs(graph, node, vis, ans)


class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
            
        vis = [0]*V
        ans = []
        
        for i in range(V):
            if vis[i] == 0:
                dfs(adj, i, vis, ans)
                
        return ans