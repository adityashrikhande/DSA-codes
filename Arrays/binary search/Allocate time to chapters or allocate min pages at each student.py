
def allocate(bar, time, n, m):
    days = 0
    sec = 0
    for i in range(m):       
        if sec + time[i] > bar:
            days += 1
            sec = time[i]
            if sec > bar:
                return False
        else:
            sec += time[i]
    if days < n:
        return True
    return False
            
def ayushGivesNinjatest(n, m, time):
    # Write your code here.
    sum = 0
    low = time[0]
    for i in range(m):
        sum += time[i]
        low = min(low, time[i])
    high = sum
    
    while low <= high:
        mid = (low + high)//2
        if allocate(mid, time, n, m):
            high = mid-1
        else:
            low = mid+1
            
    return low