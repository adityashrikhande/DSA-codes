
def rotate(head, k):
    # Write your code here.
    if k == 0:
        return head
    nhead = None
    cut = None
    end = None
    n = 0
    temp = head
    while temp != None:
        temp = temp.next
        n += 1
    if k > n:
        k = k%n
    if n == k:
        return head
    temp = head
    cnt = 1
    while temp != None:
        if n-k == cnt:
            cut = temp
        if n-k+1 == cnt:
            nhead = temp
        if n == cnt:
            end = temp
        cnt += 1
        temp = temp.next
    
    end.next = head
    cut.next = None
    
    return nhead
    