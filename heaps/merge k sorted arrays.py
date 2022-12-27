
from heapq import heapify, heappop, heappush
def mergeKSortedArrays(kArrays, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
    heap = []
    ans = []
    heapify(heap)
    for i in range(k):
        heappush(heap, [kArrays[i][0], i, 0])
    
    while len(heap) > 0:
        temp = heappop(heap)
        ans.append(temp[0])
        if temp[2]+1 < len(kArrays[temp[1]]):
            heappush(heap, [kArrays[temp[1]][temp[2]+1], temp[1], temp[2]+1])
            
    return ans
    
    