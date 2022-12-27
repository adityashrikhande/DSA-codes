
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        flag = 0

        if head == None or head.next == None:
            return None

        while slow != None and fast != None:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                break
            if fast == slow:
                flag = 1
                break
        if flag == 0:
            return None
        else:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            
            return slow
    