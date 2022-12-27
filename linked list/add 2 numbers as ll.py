
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def addTwoNumbers(head1, head2):
    # Write your code here.
    temp = head1
    n1 = 0
    n2 = 0
    while temp != None:
        n1 += 1
        temp = temp.next
    
    temp = head2
    while temp != None:
        n2 += 1
        temp = temp.next
    
    
    carry = 0
    flag = 0
    if n1 >= n2:
        temp1 = head1
        temp2 = head2
    else:
        flag = 1
        temp1 = head2
        temp2 = head1
    while temp2 != None:
        m = temp2.data + temp1.data + carry
        temp1.data = m%10
        carry = m//10
        if temp1.next == None:
            store = temp1
        temp1 = temp1.next
        temp2 = temp2.next
    while temp1 != None:
        if temp1.next == None:
            store = temp1
        m = temp1.data + carry
        temp1.data = m%10
        carry = m//10
        temp1 = temp1.next
    if carry != 0:
        du = Node(carry)
        store.next = du
    
    if flag == 0:
        return head1
    else:
        return head2
    
    
    
            