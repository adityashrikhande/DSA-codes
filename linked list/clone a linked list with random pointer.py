
# O(N) time and O(N) space comp

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        

def cloneRandomList(head):
    # Your code goes here.
    d = {}
    if head == None:
        return head
    temp = head
    while temp != None:
        du = LinkedListNode(temp.data)
        d[temp] = du
        temp = temp.next
    temp = head
    while temp != None:
        node = d[temp]
        if temp.next != None:
            node.next = d[temp.next]
        if temp.random != None:
            node.random = d[temp.random]
        temp = temp.next
        
    return d[head]

    

# O(N)time and O(1) space

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        

def cloneRandomList(head):
    # Your code goes here.
    temp = head
    flag = 0
    start = None
    while temp != None:
        du = LinkedListNode(temp.data)
        if flag == 0:
            start = du
            flag = 1
        t = temp.next
        temp.next = du
        du.next = t
        temp = temp.next.next
    
    temp = head
    while temp != None:
        if temp.random != None:
            temp.next.random = temp.random.next
        temp = temp.next.next
    
    temp = head
    while temp != None:
        t = temp.next
        temp.next = temp.next.next
        if temp.next != None:
            t.next = temp.next.next
        temp = temp.next
    
    return start
    
