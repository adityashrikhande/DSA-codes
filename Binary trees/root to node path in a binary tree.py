
def dfs(root, ans, B):
    
    if root == None:
        return False
    
    ans.append(root.val)
      
    if root.val == B:
        return True
    
    if dfs(root.left, ans, B):
        return True
    if dfs(root.right, ans, B):
        return True
    
    ans.pop()
    
    return False


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root, B):
        
        ans = []
        dfs(root, ans, B)
        
        return ans    