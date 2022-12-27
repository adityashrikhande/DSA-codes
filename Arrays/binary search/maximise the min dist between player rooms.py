
def allocate(mid, positions, n, c):
    players = 1
    dist = positions[0]
    for i in range(1, n):
        if positions[i]-dist >= mid:
            players += 1
            dist = positions[i]   
    if players < c:
        return False
    return True        

def chessTournament(positions, n , c):
    low = 1
    high = 1
    ans = 0
    positions.sort()
    high = positions[n-1] - positions[0]
    while low <= high:
        mid = (low+high)//2
        if allocate(mid, positions, n, c):
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans
        