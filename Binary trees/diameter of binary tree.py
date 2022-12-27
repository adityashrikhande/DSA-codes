
def height(root):
    global diameter
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    diameter = max(diameter, lh + rh)
    
    return 1 + max(lh, rh)

def diameterOfBinaryTree(root):
	# Write your code here
	# Return the root of the tree
    global diameter
    diameter = 0
    if root == None:
        return 0
    height(root)
    
    return diameter