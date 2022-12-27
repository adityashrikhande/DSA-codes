
class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def serializeTree(root):
	#	Write your code here for serialization of the tree.
    if root == None:
        return ''
    s = ''
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node != None:
            s += str(node.data)+','
        else:
            s += '#,'
        if node != None:
            q.append(node.left)
            q.append(node.right)
    return s
    
def deserializeTree(s):
	#	Write your code here for deserialization of the tree.
    n = len(s)
    if n == 0:
        return None
    q = []
    i = 0
    st = ''
    while s[i] != ',':
        st += s[i]
        i += 1
    i += 1
    root = TreeNode(int(st))
    q.append(root)
    
    while len(q):
        node = q.pop(0)
        st = ''
        while s[i] != ',':
            st += s[i]
            i += 1
        i += 1
        if st != '#':
            left = TreeNode(int(st))
            node.left = left
            q.append(left)
        
        st = ''
        while s[i] != ',':
            st += s[i]
            i += 1
        i += 1
        if st != '#':
            right = TreeNode(int(st))
            node.right = right
            q.append(right)
        
        if i == n-1:
            break
    
    return root
        