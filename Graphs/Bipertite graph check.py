
# BFS

class Solution(object):
    
    def check(self, graph, node, color):
        
        q = []
        q.append(node)
        color[node] = 1
        
        while len(q) != 0:
            
            nod = q.pop(0)
            
            for i in graph[nod]:
                if color[i] != -1:
                    if color[i] == color[nod]:
                        return False
                else:
                    color[i] = 1 - color[nod]
                    
                    q.append(i)
        
        return True
                        
                
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        
        color = [-1 for i in range(n)]
        
        for i in range(n):
            if color[i] == -1:
                if self.check(graph, i, color) == False:
                    return False
            
        return True

# DFS

class Solution(object):
    
    def check(self, graph, node, color):
        
        if color[node] == -1:
            color[node] = 1
        
        for i in graph[node]:
            if color[i] != -1:
                if color[i] == color[node]:
                    return False
            else:
                color[i] = 1 - color[node]
                if self.check(graph, i, color) == False:
                    return False
                
        return True
                        
            
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        
        color = [-1 for i in range(n)]
        
        for i in range(n):
            if color[i] == -1:
                if self.check(graph, i, color) == False:
                    return False
            
        return True
