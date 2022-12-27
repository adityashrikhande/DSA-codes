class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()

        
def dfs(node, copy, vis):    
    vis[copy.data] = copy
    for i in node.neighbours:
        if vis[i.data] == None:
            new = graphNode(i.data)    
            copy.neighbours.append(new)
            dfs(i, new, vis)
        else:
            copy.neighbours.append(vis[i.data])
    
def cloneGraph(node):
    # Write your code here.
    
    vis = [None for i in range(int(1e5+3))]    
    copy = graphNode(node.data)    
    dfs(node, copy, vis)
    
    return copy
    