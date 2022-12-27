
def lca(root, x, y):
    if root == None or root.data == x or root.data == y:
        return root
    
    left = lca(root.left, x, y)
    right = lca(root.right, x, y)
    
    if left == None:
        return right
    elif right == None:
        return left
    else:
        return root
        

def lowestCommonAncestor(root, x, y):
    # Write your code here.
    ans = lca(root, x, y)
    if root == None:
        return -1
    return ans.data
    