
def multi(number, n):
    ans = 1
    for i in range(n):
        ans *= number
    return ans

def findNthRootOfM(n,m):
    # Write your Code here.
    low = 1
    high = m
    while (high-low) > 1e-7:
        mid = (high+low)/2
        if multi(mid, n) < m:
            low = mid
        else:
            high = mid
    
    return '{:.6f}'.format(high)
    