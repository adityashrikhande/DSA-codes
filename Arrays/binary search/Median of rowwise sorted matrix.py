
def count(row, mid):
    low = 0
    high = len(row)-1
    while low <= high:
        m = (high+low)//2
        if row[m] <= mid:
            low = m+1
        else:
            high = m-1
    return low

def getMedian(matrix):
    # Write your code here.
    n = len(matrix)
    m = len(matrix[0])
    
    low = 1
    high = 1e9
    while low <= high:
        mid = (low+high)//2
        cnt = 0
        for i in range(n):
            cnt += count(matrix[i], mid)
        if cnt <= (n*m)//2:
            low = mid+1
        else:
            high = mid-1
            
    return int(low)       
    
