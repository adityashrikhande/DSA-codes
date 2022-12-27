
import math
 
# Link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def kAltReverse(head, k):
    
    cur = head
    next = None
    prev = None
    
    count = 0
    
    while cur != None and count < k:
        
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        count += 1
        
    if head != None:
        head.next = cur
    
    count = 0   
    while count < k-1 and cur != None:
        cur = cur.next
        count += 1
    
    if cur != None:
        cur.next = kAltReverse(cur.next, k)
        
    return prev
    
    
def push(head_ref, new_data):
     
    # allocate node
    new_node = Node(new_data)
 
    # put in the data
    # new_node.data = new_data
 
    # link the old list off the new node
    new_node.next = head_ref
 
    # move the head to po to the new node
    head_ref = new_node
     
    return head_ref
 
# Function to print linked list
def printList(node):
    count = 0
    while(node != None):
        print(node.data, end = " ")
        node = node.next
        count = count + 1
     
# Driver code
if __name__=='__main__':
     
    # Start with the empty list
    head = None
 
    # create a list 1.2.3.4.5...... .20
    for i in range(20, 0, -1):
        head = push(head, i)
         
    print("Given linked list ")
    printList(head)
    head = kAltReverse(head, 3)
 
    print("\nModified Linked list")
    printList(head)
     