
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):

        n = len(A)
        m = len(A[0])

        if n == 1:
            return A[0]

        lon_pref = ""
        j = 0
        flag = 0

        while j < m:

            for i in range(n-1):
                if j < len(A[i]) and j < len(A[i+1]) and A[i][j] == A[i+1][j]:
                    continue
                else:
                    flag = 1
                    break

            if flag == 0:
                lon_pref += A[i][j]
            else:
                break
            
            j += 1

        return lon_pref

              