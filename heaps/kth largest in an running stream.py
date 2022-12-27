
from heapq import heapify, heappush, heappop
def Kthlargest(k,arr):
    # Write your code here.
    global heap
    heap = []
    heapify(heap)
    i = 0
    while len(heap) < k:
        heappush(heap, arr[i])
        i += 1
        
def add(num):
    global heap
    # Write your code here.
    heappush(heap, num)
        
def getKthLargest():
    global heap
    # Write your code here.
    while len(heap) > k:
        heappop(heap)
    return heap[0]
        