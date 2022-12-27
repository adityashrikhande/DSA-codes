
from heapq import heapify, heappop, heappush
def findMedian(arr, n):
    # Write your code here
    if n == 0:
        return []
    minheap = []
    maxheap = []
    heapify(maxheap)
    heapify(minheap)
    heappush(maxheap,(-1)*(arr[0]))
    ans = [arr[0]]
    for i in range(1, n):
        #rint(maxheap, minheap)
        if arr[i] > (-1)*maxheap[0]:
            heappush(minheap, arr[i])
        else:
            heappush(maxheap,(-1)*(arr[i]))
        #rint(maxheap, minheap)
        if len(maxheap) > len(minheap)+1:
            temp = heappop(maxheap)
            heappush(minheap, -1*temp)
        elif len(maxheap) <len(minheap):
            temp = heappop(minheap)
            heappush(maxheap,(-1)*temp)
        #rint(maxheap, minheap)    
        if (i+1)%2 == 0:
            ans.append((minheap[0] + (-1)*maxheap[0])//2)
        else:
            ans.append((-1)*maxheap[0])
   
    for e in ans:
        print(e, end = " ")
    print()
                