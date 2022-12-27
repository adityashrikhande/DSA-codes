
# O(N) time O(H) space

def solve(root):
    l = 1
    r = 1
    if root.left:
        l = 1 + solve(root.left)
    if root.right:
        r = 1 + solve(root.right)
    
    return max(l, r)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        return solve(root)
        
        