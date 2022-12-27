
class Solution:
    
    def maxhist(self,A, n):
        
        ps = []
        ns = []
        
        st = []
        ptr = -1
        
        maxans = 0
        
        for i in range(n):
            
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
        
        for i in range(n-1, -1, -1):
            
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
            ns[l], ns[r] = ns[r], ns[l]
            l += 1
            r -= 1
            
        for i in range(n):
            
            temp = (ns[i]-ps[i]-1) * A[i]
            
            maxans = max(maxans, temp)
            
        return maxans
        
        
    
    
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        
        arr = matrix[0]
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(n):
            if arr[i] == '1':
                arr[i] = 1
            else:
                arr[i] = 0
        
        ans = self.maxhist(arr, n)
        
        for i in range(1,m):
            for j in range(n):
                
                if matrix[i][j] == '1':
                    arr[j] += 1
                else:
                    arr[j] = 0
                    
            ans = max(ans, self.maxhist(arr, n))
            
        return ans