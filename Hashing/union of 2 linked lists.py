
def union(head1,head2):
    # code here
    # return head of resultant linkedlist
    s = set()
    
    temp = head1
    
    while temp.next != None:
        s.add(temp.data)
        temp = temp.next
        
    s.add(temp.data)
        
    temp.next = head2
    temp = head2
    
    while temp.next != None:
        s.add(temp.data)
        temp = temp.next
        
    s.add(temp.data)
        
    li = list(s)
    
    li.sort()
    
    temp = head1
    
    for i in range(len(li)-1):
        temp.data = li[i]
        temp = temp.next
        
    temp.data = li[-1]
        
    temp.next = None
        
    return head1
    
    
        