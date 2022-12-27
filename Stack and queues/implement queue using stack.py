from collections import deque

class MyQueue:

    def __init__(self):
        self.st1 = deque()
        self.st2 = deque()

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        
        if len(self.st2) != 0:
            return self.st2.pop()
        else:
            
            for i in range(len(self.st1)):
                self.st2.append(self.st1.pop())
            
            return self.st2.pop()
            

    def peek(self) -> int:
        
        if len(self.st2) != 0:
            return self.st2[-1]
        else:
            
            for i in range(len(self.st1)):
                self.st2.append(self.st1.pop())
            
            return self.st2[-1]

    def empty(self) -> bool:
        return (len(self.st1) == 0 and len(self.st2) == 0)
