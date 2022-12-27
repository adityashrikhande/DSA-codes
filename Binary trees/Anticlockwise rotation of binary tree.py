
def inorder(root, ans):
    if root == None:
        return
    if root.left == None and root.right == None:
        ans.append(root.data)
    inorder(root.left, ans)
    inorder(root.right, ans)
    
        
def traverseBoundary(root):
    # Write your code here.
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.data]
    ans = [root.data]
    cur = root.left
    while True:
        if cur == None or (cur.left == None and cur.right == None):
            break
        ans.append(cur.data)
        if cur.left == None:
            cur = cur.right
        else:
            cur = cur.left
    
    inorder(root, ans)
    st = []
    cur = root.right
    while True:
        if cur == None or (cur.left == None and cur.right == None):
            break
        st.append(cur.data)
        if cur.right == None:
            cur = cur.left
        else:
            cur = cur.right
    
    while len(st) > 0:
        ans.append(st.pop())
    
    return ans