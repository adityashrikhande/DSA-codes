
# 2N space
class MinStack(object):

    def __init__(self):
        # Write your code here.
        self.st = []
    
    # Function to add another element equal to num at the top of stack.
    def push(self, num):
        # Write your code here.
        mini = 1e9
        if len(self.st) == 0:
            mini = num
        else:
            mini = min(self.st[-1][1], num)
        self.st.append([num, mini])
    
    # Function to remove the top element of the stack.
    def pop(self):
        # Write your code here.
        if len(self.st) != 0:
            return self.st.pop()[0]
        else:
            return -1
    
    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self):
        # Write your code here.
        if len(self.st) == 0:
            return -1
        else:
            return self.st[-1][0]
    
    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self):
        # Write your code here.
        if len(self.st) == 0:
            return -1
        else:
            return self.st[-1][1]
        
# N space

class MinStack(object):

    def __init__(self):
        # Write your code here.
        self.st = []
        self.mini = 1e9+1
    
    # Function to add another element equal to num at the top of stack.
    def push(self, num):
        # Write your code here.
        val = num
        if len(self.st) == 0:
            self.mini = val
            self.st.append(val)
        else:
            if val < self.mini:
                self.st.append(2*val - self.mini)
                self.mini = val
            else:
                self.st.append(val)
    
    # Function to remove the top element of the stack.
    def pop(self):
        # Write your code here.
        if len(self.st) != 0:
            temp = self.st.pop()
            if temp < self.mini:
                self.mini = 2*self.mini - temp
                return self.mini
            return temp
        else:
            return -1
    
    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self):
        # Write your code here.
        if len(self.st) == 0:
            return -1
        else:
            if self.st[-1] < self.mini:
                return self.mini
            return self.st[-1]
    
    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self):
        # Write your code here.
        if len(self.st) == 0:
            return -1
        else:
            return self.mini
        