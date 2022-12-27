
# 2 stack approach

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        
        s1 = [A]
        s2 = []
        
        ans = []
        
        while len(s1) != 0:
            node = s1.pop()
            s2.append(node)
            
            if node.left != None:
                s1.append(node.left)
            
            if node.right != None:
                s1.append(node.right)
                
        while len(s2) != 0:
            ans.append(s2.pop().val)
            
        return ans


# 1 stack approach  somewhat complex

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        
        st = []
        cur = A
        
        ans = []
        
        while cur != None or len(st) != 0:
            
            if cur != None:
                st.append(cur)
                cur = cur.left
            
            else:

                temp = st[-1].right
                
                if temp == None:
                    temp = st[-1]
                    ans.append(temp.val)
                    st.pop()
                    
                    while len(st) != 0 and temp == st[-1].right:
                        temp = st[-1]
                        st.pop()
                        ans.append(temp.val)
                else:
                    cur = temp
                           
        return ans
                    