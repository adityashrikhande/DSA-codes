
def solve(root, di):
    if root == None:
        return
    q = [(root, 0)]
    di[0] = root.data
    while len(q) > 0:
        temp = q.pop(0)
        idx = temp[1]
        node = temp[0]
        di[idx] = node.data
        if node.left != None:
            q.append((node.left, idx-1))
    
        if node.right != None:
            q.append((node.right, idx+1))
            
                
def bottomView(root):
    
    # Write your code here.
    # This function returns a list of nodes which is the required bottom view of the tree.
    di = {}
    ans = []
    solve(root, di)
    for i in di.keys():
        ans.append((i, di[i]))
    ans = sorted(ans, key = lambda x: x[0])
    n = len(ans)
    for i in range(n):
        ans[i] = ans[i][1]
    return ans