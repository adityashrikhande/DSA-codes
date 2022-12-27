
def ninjaAndLadoos(row1, row2, m, n, k):
    # Write your code here.
    if n > m:
        ninjaAndLadoos(row2, row1, n, m, k)
    low = max(0, k-n)
    high = min(k, m)
    
    while low <= high:
        cut1 = (low + high)//2
        cut2 = k-cut1
        if cut1 == 0:
            l1 = 1e-9
        else:
            l1 = row1[cut1-1]
        if cut2 == 0:
            l2 = 1e-9
        else:
            l2 = row2[cut2-1]
        if cut1 == m:
            r1 = 1e9
        else:
            r1 = row1[cut1]
        if cut2 == n:
            r2 = 1e9
        else:
            r2 = row2[cut2]
            
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
        
    return -1
        