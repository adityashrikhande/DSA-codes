
from heapq import heapify, heappop, heappush
def kMaxSumCombination(a, b, n, k):
	# Write your code here.
    a.sort()
    b.sort()
    ans = []
    li = []
    li.append([n-1, n-1])
    heap = []
    heapify(heap)
    heappush(heap, [(-1)*(a[n-1] + b[n-1]), [n-1, n-1]])
    while k:
        top = heappop(heap)
        ans.append((-1)*top[0])
        m = top[1]
        #print(m)
        l = m[0]
        r = m[1]
        if l > 0 and r > 0 and [l-1, r] not in li:
            heappush(heap, [(-1)*(a[l-1] + b[r]), [l-1, r]])
            li.append([l-1, r])
        if l > 0 and r > 0 and [l, r-1] not in li:
            heappush(heap, [(-1)*(a[l] + b[r-1]), [l, r-1]])
            li.append([l, r-1])
            
        k -= 1
        
    return ans
        