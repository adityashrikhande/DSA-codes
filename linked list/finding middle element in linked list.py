
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        
        temp = head
        len1 = 1
        
        while temp.next != None:
            temp = temp.next
            len1 += 1
            
        mid = len1//2 + 1
        
        k = 1
        
        temp = head
        
        if k == mid:
            return temp.data
        
        while temp.next != None:
            temp = temp.next
            k += 1
            
            if k == mid:
                return temp.data
            