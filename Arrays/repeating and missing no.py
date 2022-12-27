
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        n = len(A)
        
        s = (n*(n+1))//2
        sq = (n*(n+1)*(2*n+1))//6
        
        m = 0      # missing
        r = 0      # repeating
        
        for i in range(n):
            s -= A[i]
            sq -= A[i]*A[i]
                                            # s = m - r ,   sq = m^2 - r^2 = (m+r)*(m-r)
        m = (s + sq//s)//2
        r = m - s
        
        return [r,m]