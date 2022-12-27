
class Solution:
    def isPalindrome(self, head):
        #code here
        
        temp = head
        n = 1
        k = 1
        
        while temp.next != None:
            temp = temp.next
            n += 1
        
        if n == 1:
            return True
            
        if n == 2 and head.data == head.next.data:
            return True
        elif n == 2:
            return False
        
        if n == 3 and head.data == head.next.next.data:
            return True
        elif n == 3:
            return False
            
            
        temp = head
        
        if n%2 == 0:
            mid = n//2
        else:
            mid = n//2 + 1
            
        
        while temp.next != None:
            temp = temp.next
            k += 1
            
            if k == mid:
                p = temp
            
            if k == mid + 1:
                break
            
        head1 = temp
        prev = head1
        nxt = head1.next
        
        prev.next = None
        
        while nxt != None:
            prev = temp
            temp = nxt
            
            nxt = nxt.next
            
            temp.next = prev
        
        p.next = temp
        
                        
        while temp != None:
            if temp.data != head.data:
                return False
            temp = temp.next
            head = head.next
                
        return True
        
                
        