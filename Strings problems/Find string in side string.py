
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        m = len(A)
        n = len(B)

        if n > m or m == 0 or n == 0:
            return -1

        i = 0
        j = n-1

        while j < m:
            
            if A[i:j+1] == B:
                return i
            
            i += 1
            j += 1

        return -1
