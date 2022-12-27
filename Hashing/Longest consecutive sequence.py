
from heapq import heappush, heappop, heapify

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    heap = []
    heapify(heap)
    
    for i in range(n):
        heappush(heap, arr[i])
    
    ans = 1
    cnt = 1
    prev = heappop(heap)
    while len(heap) != 0:
        cur = heappop(heap)
        if cur == prev + 1:
            cnt += 1
            ans = max(ans, cnt)
        elif cur == prev:
            pass
        else:
            cnt = 1
        prev = cur
    
    return ans
    
    