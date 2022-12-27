
class Solution:
    def reverse(self,head, k):
        # Code here
        
        curr = head
        nex = head
        prev = None
        count = 0
        
        while nex != None and count < k:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            count += 1
            
        if nex != None:
            head.next = self.reverse(nex, k)
            
        return prev

# Another approach with array b having different k values

def reverse(head, n, i, b):
    cur = head
    nex = head
    prev = None
    cnt = 0
    
    while i < n and b[i] == 0:
        i += 1
    
    if i == n:
        return head
    
    while nex != None and cnt < b[i]:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex
        cnt += 1
    
    if nex != None:
        head.next = reverse(nex, n, i+1, b)
    
    return prev
        

def getListAfterReverseOperation(head, n, b):
    # Write your code here.
    return reverse(head, n, 0, b)
                     


#other solution , keeping last elements < k constant
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or k == 1:
            return head
        
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        pre = dummy
        nex = dummy
        
        count = 0
        
        while cur.next != None:
            cur = cur.next
            count += 1
            
        while count >= k:
            cur = pre.next
            nex = cur.next
            
            for i in range(k-1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
                
            pre = cur
            count -= k
            
        return dummy.next
        
"""