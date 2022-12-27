
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)

        if (n == 1):
            return 1

        i = 0
        j = 1
        
        while j < n and i < n:
            while j < n and A[j] == A[i]:
                j += 1
            if j < n:
                i += 1
                A[i] = A[j]
            
        return i + 1