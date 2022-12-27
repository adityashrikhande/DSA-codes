
from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        heap = []
        
        heapify(heap)
        
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
            
        return heappop(heap)

# using minheap approach IMP

from heapq import heapify, heappop, heappush

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        heap = []
        
        ans = []
        
        #heapify(heap)
        
        for num in A:
            heappush(heap, num*(-1))      # putting num in heap as -ve so max element come at top with -ve sign
        
        for i in range(B):   
            ans.append(heappop(heap)*(-1))  # popping maxelement with -ve sign and converting into +ve 
            
        return ans