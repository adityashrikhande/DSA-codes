
class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):

        n = len(A)

        if n == 1:
            return A

        i = 0
        j = 0

        ans = ""

        for k in range(n):

            i = k
            j = k

            while i >= 0 and j < n and A[i] == A[j]:
                i -= 1
                j += 1

            if j-i-1 > len(ans):
                ans = A[i+1:j]

        for k in range(n-1):

            if A[k] == A[k+1]:
                i = k
                j = k+1

                while i >= 0 and j < n and A[i] == A[j]:
                    i -= 1
                    j += 1

                if j-i-1 > len(ans):
                    ans = A[i+1:j]
            
        return ans