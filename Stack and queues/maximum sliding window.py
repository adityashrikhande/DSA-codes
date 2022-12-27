
# nlogn time heap

from heapq import heapify, heappop, heappush
def slidingWindowMaximum(nums:list, k:int):
	# Write your code here
	# Return a list
    heap = []
    heapify(heap)
    ans = []
    n = len(nums)
    for i in range(k):
        heappush(heap, [(-1)*nums[i], i])
    ans.append((-1)*heap[0][0])
    
    for i in range(k, n):
        while len(heap) > 0 and heap[0][1] <= i-k:
            heappop(heap)
        heappush(heap, [(-1)*nums[i], i])
        ans.append((-1)*heap[0][0])
    
    return ans

# O(N) solution deque

from heapq import heapify, heappop, heappush
def slidingWindowMaximum(nums:list, k:int):
	# Write your code here
	# Return a list
    ans = []
    arr = []
    n = len(nums)
    for i in range(n):
        if len(arr) != 0 and arr[0] == i-k:
            arr.pop(0)
        while len(arr) != 0 and nums[arr[-1]] < nums[i]:
            arr.pop()
        arr.append(i)
        if i+1 >= k:
            ans.append(nums[arr[0]])
    
    return ans