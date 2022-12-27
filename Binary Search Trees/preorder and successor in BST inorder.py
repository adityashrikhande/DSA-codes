
def find(root, key):
    global pre, suc, flag
    if root == None:
        return root
    find(root.left, key)
    if root.data < key:
        pre = root.data
    elif flag == False and root.data > key:
        suc = root.data
        flag = True
    find(root.right, key)
    
def predecessorSuccessor(root, key):
    # Write your code here.
    global pre, suc, flag
    flag = False
    pre = -1
    suc = -1
    find(root, key)

    return pre, suc
    
