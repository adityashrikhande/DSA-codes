
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        
        arr = [-1]
    
        st = [A[0]]
        ptr = 0
        
        for i in range(1,len(A)):
            
            while ptr >= 0 and st[ptr] >= A[i]:
                st.pop()
                ptr -= 1
            
            if ptr == -1:
                arr.append(-1)
            else:
                arr.append(st[ptr])
                
            st.append(A[i])
            ptr += 1
            
            
                
        return arr   