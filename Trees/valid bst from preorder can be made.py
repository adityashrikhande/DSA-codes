
class Solution:
    # @param A : list of integers
    # @return an integer
    
    def check(self, A):
        st = []
        root = -2**32
        
        for i in A:
            
            if i < root:
                return 0
            
            while (len(st) > 0 and i > st[-1]):
                
                root = st.pop()
            
            st.append(i)
            
        return 1
                
    
    def solve(self, A):
        
        return self.check(A)
                