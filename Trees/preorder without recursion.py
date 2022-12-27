
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        
        if A == None:
            return []
        q = [A]
        ans = []
        
        while len(q) != 0:
            
            node = q.pop()
            ans.append(node.val)
            
            if node.right != None:
                q.append(node.right)
                
            if node.left != None:
                q.append(node.left)
                
        return ans
