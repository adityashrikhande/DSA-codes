
def calculateMinPatforms(at, dt, n):
    # Write your code here.
    at.sort()
    dt.sort()
    ans = 1
    cnt = 1
    i = 0
    j = 1
    while j < n and i < n:
        if at[j] <= dt[i]:
            j += 1
            cnt += 1
        else:
            cnt -= 1
            i += 1
        ans = max(cnt, ans)
    
    return ans