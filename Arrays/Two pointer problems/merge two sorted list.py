
def merge(self, A, B):

        m = len(A)
        n = len(B)

        i = 0
        j = 0
        
        while i < len(A) and j < n:
            if A[i] >= B[j]:
                A.insert(i, B[j])
                j += 1
                i += 1
                
            else:
                i += 1
            if i == len(A):
                A.append(0)
                A[i] = B[j]
                j += 1
        