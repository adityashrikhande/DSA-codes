
class BSTiterator:
    def __init__(self, root, reverse):
        self.root = root
        self.st = []
        self.reverse = reverse
        self.pushall(root, reverse)
    
    def next(self, reverse):        
        temp = self.st.pop()
        if not reverse:
            self.pushall(temp.right, reverse)
        else:
            self.pushall(temp.left, reverse)
        return temp.data
    
    def pushall(self, node, reverse):
        while node != None:
            if not reverse:
                self.st.append(node)
                node = node.left
            else:
                self.st.append(node)
                node = node.right
        
def pairSumBST(root, k):
	# Write your code here
    l = BSTiterator(root, False)
    r = BSTiterator(root, True)
    
    i = l.next(False)
    j = r.next(True)
    
    while i < j:
        if i+j == k:
            return True
        elif i+j < k:
            i = l.next(False)
        else:
            j = r.next(True)
    
    return False
    