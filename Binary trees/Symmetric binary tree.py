
def dfs(r1, r2):
    global flag
    if r1 == None and r2 == None:
        return
    if (r1 != None and r2 == None) or (r1 == None and r2 != None) or r1.data != r2.data:
        flag = False
        return
    
    dfs(r1.left, r2.right)
    if not flag:
        return
    dfs(r1.right, r2.left)
    if not flag:
        return
    
def isSymmetric(root) :
    # Write your code here.
    global flag
    flag = True
    
    dfs(root, root)
    
    return flag