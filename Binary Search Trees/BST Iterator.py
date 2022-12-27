
class BSTiterator:
    def __init__(self, root):
        # Complete the constructor function
        self.st = []
        temp = root
        while temp != None:
            self.st.append(temp)
            temp = temp.left
        self.root = root

    def next(self):
        # Complete the functiom
        if len(self.st) == 0:
            return -1
        else:
            temp = self.st.pop()
            if temp.right != None:
                node = temp.right
                while node != None:
                    self.st.append(node)
                    node = node.left
            return temp.data
                

    def hasNext(self):
        # Complete the function
        if len(self.st) == 0:
            return False
        else:
            return True
        