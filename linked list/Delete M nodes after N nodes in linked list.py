
class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        
        temp = head
        
        k = 1
        k2 = 0
        
        while temp != None:
            
            if k == M:
                prev = temp
                i = 0
                while temp != None and i < N:
                    temp = temp.next
                    i += 1
                if temp != None: 
                    prev.next = temp.next
                else:
                    prev.next = None
                k = 0
            
            if temp != None:    
                temp = temp.next
                
            k += 1
                