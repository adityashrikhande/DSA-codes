
# Iterative solution

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        
        qe = [A]
        st = []
        ans = [A.val]
        
        while True:
            
            node = qe[0]
            qe.pop(0)
            
            if node.left != None:
                st.append(node.left)
            if node.right != None:
                st.append(node.right)
            
            if len(qe) == 0:
                if len(st) == 0:
                    break
                ans.append(st[-1].val)
                qe = st
                st = []
        
        return ans    

# Recursive solution   

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    
    def rec(self, root, level, ans):
        
        if root == None:
            return
        
        if len(ans) == level:
            ans.append(root.val)
            
        self.rec(root.right, level + 1, ans)
        self.rec(root.left, level + 1, ans)
            
    
    def solve(self, root):
        
        ans = []
        
        self.rec(root, 0, ans)
        
        return ans             