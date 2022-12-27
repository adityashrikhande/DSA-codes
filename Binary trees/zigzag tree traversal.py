
def reverse(arr):
    l = 0
    r = len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
    return arr

def zigZagTraversal(root):
    # Write your code here
    if root == None:
        return []
    q = [root]
    q1 = []
    check = 1
    ans = [root.data]
    temp = []
    while True:
        while len(q) != 0:       
            node = q.pop(0)

            if node.left != None:
                q1.append(node.left)
                temp.append(node.left.data)
            if node.right != None:
                q1.append(node.right)
                temp.append(node.right.data)
        if len(q1) == 0:
            break
        q = q1
        if check:
            ans.extend(reverse(temp))
        else:
            ans.extend(temp)
        check = check^1
        temp = []
        q1 = []
    
    return ans
        
        