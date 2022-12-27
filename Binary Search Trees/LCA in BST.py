
def LCA(root, p, q):

    if root == None or root.data == p.data or root.data == q.data:
        return root
    
    left = None
    right = None
    
    if root.data > p.data and root.data > q.data:
        left = LCA(root.left, p, q)
    elif root.data < p.data and root.data < q.data:
        right = LCA(root.right, p, q)
    else:
        left = LCA(root.left, p, q)
        right = LCA(root.right, p, q)
        
    if left == None:
        return right
    elif right == None:
        return left
    else:
        return root
     

def LCAinaBST(root, P, Q):
    # Write your code here
    # P and Q are the given nodes
    # Return LCA node
    
    ans = LCA(root, P, Q)
    
    return ans