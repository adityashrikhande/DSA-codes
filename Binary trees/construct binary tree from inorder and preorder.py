
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build(preorder, inorder, l, r, a, b, d):
    if l > r or a > b:
        return None
    root = BinaryTreeNode(preorder[l])
    anchor = d[root.data]
    #ele = anchor - a
    root.left = build(preorder, inorder, l+1, l +anchor-a, a, anchor-1, d)
    root.right = build(preorder, inorder, l + anchor-a +1, r, anchor +1, b, d)
    
    return root
    
def buildBinaryTree(preorder:list, inorder:list):

    # Write your code here.
    # Return root node of tree.
    n = len(inorder)
    d = {}
    for i in range(n):
        d[inorder[i]] = i
    return build(preorder, inorder, 0, n-1, 0, n-1, d)

