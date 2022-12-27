
def Convert(root):
    global prev, head
    if root == None:
        return
    
    Convert(root.left)
    if prev == None:
        head = root
    else:
        root.left = prev
        prev.right = root
    
    prev = root
    Convert(root.right)
    
       
def BTtoDLL(root):
    # Write your code here.
    global prev, head
    head = None
    prev = None
    
    Convert(root)
    
    return head
        