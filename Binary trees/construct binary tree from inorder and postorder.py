
def Build(postOrder, inOrder, ps, pe, ins, ine, d):
    if ps > pe or ins > ine:
        return None
    anchor = d[postOrder[pe]]
    ele = anchor-ins
    root = TreeNode(postOrder[pe])
    
    root.left = Build(postOrder, inOrder, ps, ps+ele-1, ins, ins+ele-1, d)
    root.right = Build(postOrder, inOrder, ps+ele, pe-1, ins+ele+1, ine, d)
    
    return root
        
        
def getTreeFromPostorderAndInorder(postOrder, inOrder):
	# Write your code here.
    n = len(postOrder)
    d = {}
    for i in range(n):
        d[inOrder[i]] = i
    
    return Build(postOrder, inOrder, 0, n-1, 0, n-1, d)