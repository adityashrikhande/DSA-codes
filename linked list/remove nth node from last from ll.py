
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def removeKthNode(head, k):
    # Write your function here.
    n = 0
    temp = head
    if head == None or k == 0:
        return head
    
    while temp != None:
        temp = temp.next
        n += 1
   
    length = n - k + 1
    
    if length == 1:
        return head.next
    
    prev = Node(-1)
    prev.next = head
    cur = head
    cnt = 1
    while cur.next != None:
        prev = prev.next
        cur = cur.next
        cnt += 1
        if cnt == length:
            break
    
    prev.next = cur.next
    cur.next = None
    
    return head