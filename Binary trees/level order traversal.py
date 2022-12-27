
def getLevelOrder(root):

    #   Write your code here
    if root == None:
        return []
    q = [root]
    ans = []
    while len(q) > 0:
        node = q.pop(0)
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return ans