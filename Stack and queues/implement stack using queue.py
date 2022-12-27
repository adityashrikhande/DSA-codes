from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()   
            
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        n = len(self.q1)
        if n == 0:
            return -1
        i = 0
        while i < n-1:
            self.q1.append(self.q1.popleft())
            i += 1
        return self.q1.popleft()
        

    def top(self) -> int:
        
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0
            