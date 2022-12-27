
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next
            
def merge(h1, h2):
    temp1 = h1
    temp2 = h2
    
    du = Node(-1)
    res = du
    
    while temp1 != None and temp2 != None:
        if temp1.data > temp2.data:
            du.child = temp2
            temp2 = temp2.child
            du = du.child
        else:
            du.child = temp1
            temp1 = temp1.child
            du = du.child
    if temp1 != None:
        du.child = temp1
    if temp2 != None:
        du.child = temp2
    
    res.next = None
    
    return res.child

def flatten(head):
    if head.next == None:
        return head
    
    head2 = flatten(head.next)
    
    ans = merge(head, head2)
    return ans

def flattenLinkedList(head):
    # write your code here
    return flatten(head)
    
    