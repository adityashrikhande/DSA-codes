
def check(root, x):
    global flag
    if root == None:
        return
    if root.data == x:
        flag = True
        return
    if x > root.data:
        check(root.right, x)
    else:
        check(root.left, x)

def searchInBST(root, x):
	# Write your code here.
    global flag
    flag = False
    
    check(root, x)
    
    return flag
    