
def height(root):
    global flag
    if root == None:
        return 0
    lh = height(root.left)
    if flag == False:
        return -1
    rh = height(root.right)
    if flag == False:
        return -1
    
    if abs(lh-rh) > 1:
        flag = False
    
    return 1 + max(lh, rh)

def isBalancedBT(root):
    # Write your code here
    # Return True/False
    global flag
    flag = True
    
    if root == None:
        return True
    
    height(root)
    
    return flag