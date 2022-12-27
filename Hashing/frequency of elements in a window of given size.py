
from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        n = len(A)
        if B > n:
            return []
        
        ans = []
        d = defaultdict(int)
        cnt = 0
        for i in range(B):   
            d[A[i]] += 1
            
        ans.append(len(d))
        
        for i in range(B, n):
            
            d[A[i]] += 1
            d[A[i-B]] -= 1
            if d[A[i-B]] == 0:
                del d[A[i-B]]
              
            ans.append(len(d))
            
        
        return ans
        
    