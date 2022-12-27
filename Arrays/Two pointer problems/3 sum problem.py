
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        
        ans = 1e9
        n = len(A)
        add = 0
        A.sort()

        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                curr_add = A[i] + A[j] + A[k]
                if curr_add > B:
                    k -= 1
                elif curr_add < B:
                    j += 1
                else:
                    return B
                if ans > abs(curr_add - B):
                    ans = abs(curr_add - B)
                    add = curr_add
        return add