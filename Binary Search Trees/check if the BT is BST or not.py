
def check(root):
    global flag
    
    if root == None:
        return
    
    if (root.left != None and root.left.data > root.data) or (root.right != None and root.right.data < root.data):
        flag = False
        return
    
    check(root.left)
    if flag == False:
        return
    check(root.right)
    
        
def validateBST(root):
    global flag
    flag = True
    
    check(root)
    
    return flag
