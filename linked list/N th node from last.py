
def getNthFromLast(head,n):
    #code here
    temp = head
    
    length = 1
    
    while temp.next != None:
        
        temp = temp.next
        length += 1
    
    len_from_start = length - n + 1
    temp = head
    k = 1
    
    if length < n:
        return -1
    
    if k == len_from_start:
        return temp.data
        
    while temp.next != None:
        
        temp = temp.next
        k += 1
        
        if k == len_from_start:
            return temp.data
        
    return -1
        
        
        
        
        
        
        
        
        