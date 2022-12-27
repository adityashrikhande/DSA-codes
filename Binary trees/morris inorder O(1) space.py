
def morrisinorder(root):
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
                cur = cur.left
            else:
                ans.append(cur.val)
                cur = cur.right
                                
    return ans
            
            
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = morrisinorder(root)
        return ans
        