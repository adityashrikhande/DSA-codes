
def morrispreorder(root):
    ans = []
    cur = root
    prev = root
    while cur != None:
        if cur.left == None:
            ans.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right != None and prev.right != cur:
                prev = prev.right
            
            if prev.right == None:
                prev.right = cur
                ans.append(cur.val)
                cur = cur.left
            else:
                cur = cur.right
                                
    return ans
            
            
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = morrispreorder(root)
        return ans
        