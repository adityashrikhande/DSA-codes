
def median(a, b):
    # Write the function here.
    n = len(a)
    m = len(b)
    if n > m:
        return median(b, a)
    
    low = 0
    high = n
    while low <= high:
        cut1 = (low+high)//2
        cut2 = (m+n+1)//2 - cut1
        if cut1 == 0:
            l1 = 1e-9
        else:
            l1 = a[cut1-1]
        if cut2 == 0:
            l2 = 1e-9
        else:
            l2 = b[cut2-1]
        if cut1 == n:
            r1 = 1e9
        else:
            r1 = a[cut1]
        if cut2 == m:
            r2 = 1e9
        else:
            r2 = b[cut2]
        
        if l1 <= r2 and l2 <= r1:
            if (n + m)%2 == 0:
                return (max(l1, l2) + min(r1, r2))/2
            else:
                return float(max(l1, l2))
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1+1
            
        