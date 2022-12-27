
def getMaxWidth(root):
    # Write your code here.
    q1 = [root]
    q2 = []
    ans = 1
    if root == None:
        return 0
    
    while True:
        ans = max(ans, len(q1))
        while len(q1) > 0:
            node = q1.pop()
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        if len(q2) == 0:
            break
        q1 = q2
        q2 = []
    
    return ans
            