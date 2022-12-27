
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        
        n = len(A)
        
        if n == 1:
            return A[0]
        
        ps = []
        ns = []
        
        ans = A[0]
        tans = 0
        
        st = []
        ptr = -1
        
        for i in range(0,n):
            
            while ptr >= 0 and A[st[ptr]] >= A[i]:
                st.pop()
                ptr -= 1
            
            if ptr == -1:
                ps.append(-1)
            else:
                ps.append(st[ptr])
                
            st.append(i)
            ptr += 1
            
        st = []
        ptr = -1
            
        for i in range(n-1,-1,-1):
            
            while ptr >= 0 and A[st[ptr]] >= A[i]:
                st.pop()
                ptr -= 1
            
            if ptr == -1:
                ns.append(n)
            else:
                ns.append(st[ptr])
                
            st.append(i)
            ptr += 1
            
        l = 0
        r = n-1
        
        while l < r:
            
            ns[l],ns[r] = ns[r], ns[l]
            l += 1
            r -= 1
            
        for i in range(n):
            
            tans = (ns[i]-ps[i]-1) * A[i]
            
            ans = max(ans, tans)
        
        
        return ans    
            