
from typing import List

from heapq import heapify, heappop, heappush
def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    mp = {}
    for i in range(n):
        if arr[i] not in mp.keys():
            mp[arr[i]] = 1
        else:
            mp[arr[i]] += 1
    
    heap = []
    for i in mp.keys():
        heap.append((-1*mp[i], i))
    
    heapify(heap)
    #print(heap)
    ans = []
    for i in range(k):
        temp = heappop(heap)
        ans.append(temp[1])
        #print(temp)
    ans.sort()
    
    return ans