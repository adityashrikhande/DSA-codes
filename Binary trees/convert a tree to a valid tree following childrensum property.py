
def Build(root):
    if root == None:
        return
    child = 0
    if root.left != None:
        child += root.left.data
    if root.right != None:
        child += root.right.data
    
    if root.data > child:
        if(root.left):
            root.left.data = root.data
        if(root.right):
            root.right.data = root.data
    else:
        root.data = child
        
    Build(root.left)
    Build(root.right)
    
    val = 0
    if root.left:
        val += root.left.data
    if root.right:
        val += root.right.data
    
    if root.left or root.right:
        root.data = val

def changeTree(root): 
    # Write your code here.
    if root == None:
        return None
    ans = Build(root)