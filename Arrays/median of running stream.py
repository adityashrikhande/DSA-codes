
from heapq import heapify, heappush, heappop

def push(maxh, minh, ele):
    if  len(maxh) > 0 and ele > -1*maxh[0]:
        heappush(minh, ele)
    else:
        heappush(maxh, -1*ele)
    
    if len(minh) > len(maxh):
        heappush(maxh, -1*heappop(minh))
    elif len(minh)+1<len(maxh):
        heappush(minh, -1*heappop(maxh))
        
def findMedian(arr, n):

    # Write your code here
    maxh=[]
    minh = []
    heapify(minh)
    heapify(maxh)
    ans = []
    
    for i in range(n):
        push(maxh, minh, arr[i])
        
        if i%2 == 0:
            ans.append(-1*maxh[0])
        else:
            ans.append((-1*maxh[0]+minh[0])//2) # 5 10 1 0 7 
    
    return ans
