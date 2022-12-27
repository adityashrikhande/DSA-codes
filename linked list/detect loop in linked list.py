
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        if head == None or head.next == None:
            return False

        while slow != None and fast != None:
            slow = slow.next
            if fast.next == None:
                break
            fast = fast.next.next
            if fast == slow:
                return True

        return False
    


class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        
        temp = head
        
        while temp.next != None:
            
            temp.data = -1
            
            if temp.next.data == temp.data:
                return True
                
            temp = temp.next
                
        return False