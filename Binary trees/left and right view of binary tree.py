
# left view

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftview(root, level, ans):
    if root == None:
        return
    if len(ans) == level:
        ans.append(root.data)
    leftview(root.left, level+1, ans)
    leftview(root.right, level+1, ans)
        
def getLeftView(root)->list:
    # Write your code here
    # Return a list
    ans = []
    leftview(root, 0, ans)
    return ans

# right view

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rightview(root, level, ans):
    if root == None:
        return
    if len(ans) == level:
        ans.append(root.data)
    rightview(root.right, level+1, ans)
    rightview(root.left, level+1, ans)
        
def getLeftView(root)->list:
    # Write your code here
    # Return a list
    ans = []
    rightview(root, 0, ans)
    return ans