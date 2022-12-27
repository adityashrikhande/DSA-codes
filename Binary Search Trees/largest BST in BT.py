
class Node:
    def __init__(self, maxvalue, minvalue, maxsize):
        self.maxvalue = maxvalue
        self.minvalue = minvalue
        self.maxsize = maxsize

def helper(root):
    if root == None:
        return Node(-1e9, 1e9, 0)
        
    l = helper(root.left)
    r = helper(root.right)
    
    if l.maxvalue < root.data and r.minvalue > root.data:
        return Node(max(root.data, r.maxvalue), min(root.data, l.minvalue), l.maxsize + r.maxsize + 1)
    
    return Node(1e9, -1e9, max(l.maxsize, r.maxsize))
        

def largestBST(root):

    # Write your code here.
    return helper(root).maxsize