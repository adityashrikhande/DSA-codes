
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        
        if head == None:
            return
        
        if head.next == None:
            print(head.data, end = " ")
            return
        
        prev = head
        temp = head
        nxt = head.next
        temp.next = None
        
        while nxt != None:
            prev = temp
            temp = nxt
            nxt = nxt.next
            
            temp.next = prev
        
        
        while temp != None:
            print(temp.data,end = " ")
            temp = temp.next
        
        
        