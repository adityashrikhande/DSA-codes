
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        
        st = []
        cur = A
        ans = []
        
        while True:
            
            if cur != None:
                st.append(cur)
                cur = cur.left
            else:
                if len(st) == 0:
                    break
                last = st[-1]
                ans.append(st.pop().val)
                cur = last.right
                
        return ans