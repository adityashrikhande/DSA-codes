# recursion
def alltraversals(root, inorder, preorder, postorder):
    if root == None:
        return
    preorder.append(root.data)
    alltraversals(root.left, inorder, preorder, postorder)
    inorder.append(root.data)
    alltraversals(root.right, inorder, preorder, postorder)
    postorder.append(root.data)
        
def getTreeTraversal(root):
    # Write your code here.
    inorder = []
    preorder = []
    postorder = []
    
    alltraversals(root, inorder, preorder, postorder)
    
    return [inorder, preorder, postorder]

# iterative

def alltraversals(root, inorder, preorder, postorder):
    st = [(root, 1)]
    if root == None:
        return
    while len(st) > 0:
        top = st.pop()
        node = top[0]
        num = top[1]
        if num == 1:
            preorder.append(node.data)
            st.append((node, 2))
            if node.left != None:
                st.append((node.left, 1))
        elif num == 2:
            inorder.append(node.data)
            st.append((node, 3))
            if node.right != None:
                st.append((node.right, 1))
        elif num == 3:
            postorder.append(node.data)
        
        
def getTreeTraversal(root):
    # Write your code here.
    inorder = []
    preorder = []
    postorder = []
    
    alltraversals(root, inorder, preorder, postorder)
    
    return [inorder, preorder, postorder]
    
    
    