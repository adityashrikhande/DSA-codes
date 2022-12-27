
class Solution(object):
    def longestValidParentheses(self, A):
        """
        :type s: str
        :rtype: int
        """
        
        if A == '':
            return 0
        st = []
        idxarr = [-1]
        ans = 0
        n = len(A)
        
        for i in range(n):
            
            if A[i] == '(':
                st.append(A[i])
                idxarr.append(i)
            else:
                if len(st) != 0 and st[-1] == '(':
                    st.pop()
                    idxarr.pop()
                    ans = max(ans, i-idxarr[-1])
                else:
                    idxarr.append(i)
                    
                    
        return ans
        