
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        
        n = len(A)
        i = n-1
        j = n-1

        ans_string = ""

        while i >= 0 and j >= 0:

            if A[i] == " ":
                i -= 1
                j = i
            else:
                break

        while i >= 0 and j >= 0:

            if A[i] == " ":
                i -= 1
                j = i
            else:
                i -= 1
                if i == -1 or A[i] == " ":
                    ans_string += A[i+1:j+1] + " "
        
        if ans_string[len(ans_string)-1] == " ":
            ans_string = ans_string[0:len(ans_string)-1]
        
        return ans_string        