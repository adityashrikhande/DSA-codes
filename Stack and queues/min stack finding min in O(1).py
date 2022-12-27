
class MinStack:
    # @param x, an integer
    def __init__(self):
        self.st = []
        self.ms = []
    
    def push(self, x):
        
        self.st.append(x)
        if len(self.ms) == 0:
            self.ms.append(x)
        else:
            if self.ms[-1] >= x:
                self.ms.append(x)
            else:
                self.ms.append(self.ms[-1])
        
        return None

    # @return nothing
    def pop(self):
        if len(self.ms) != 0:
            self.st.pop()
            self.ms.pop()
        
    # @return an integer
    def top(self):
        if len(self.st) != 0:    
            return self.st[-1]
        return -1
    # @return an integer
    def getMin(self):
        if len(self.ms) != 0:    
            return self.ms[-1]
        return -1