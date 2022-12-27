
def add(heap, ele):
    low = 0
    high = len(heap)-1
    while low <= high:
        mid = (low+high)//2
        if ele < heap[mid]:
            high = mid-1
        else:
            low = mid+1
    if len(heap) == 0:
        heap.append(ele)
    elif len(heap) == 1:
        if heap[0] > ele:
            heap.insert(0, ele)
        else:
            heap.append(ele)
    else:
        heap.insert(low, ele)

def minHeap(N: int, Q): # Q -> [[]]
    # Write your code frome here.
    ans = []
    heap = []
    n = len(Q)
    for i in range(n):
        if Q[i][0] == 1:
            ans.append(heap.pop(0))
        else:
            add(heap, Q[i][1])
    
    return ans
