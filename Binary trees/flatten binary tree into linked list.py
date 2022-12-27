
def build(root):
    global last
    if root == None:
        return None
    if root.left == None and root.right == None:
        last = root
        return root

    left = build(root.left)
    left_final = last
    right = build(root.right)
    
    temp = root.right
    if left != None:
        root.right = left
    if left_final != None:
        left_final.right = temp
    
    return root
          
def flattenBinaryTree(root):
    # Write your code here.
    global last
    last = None
    return build(root)