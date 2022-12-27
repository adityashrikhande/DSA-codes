
def solve(r1, r2):
    global flag
    if (r1 == None and r2 != None) or (r1 != None and r2 == None) or (r1 != None and r1.data != r2.data):
        flag = False
        return
    
    if r1 == None and r2 == None:
        return
    
    solve(r1.left, r2.left)
    if flag == False:
        return
    solve(r1.right, r2.right)
    if flag == False:
        return
        
        
def identicalTrees(root1, root2):
    #Your code goes here.
    global flag
    flag = True
    solve(root1, root2)
    
    return flag