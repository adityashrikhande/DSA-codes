
def inorder(root, st):
    inord = []
    cur = root
    while True:
        if cur != None:
            st.append(cur)
            cur = cur.left
        else:
            if len(st) == 0:
                break
            cur = st.pop()
            inord.append(cur.val)
            cur = cur.right
    return inord
            
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = inorder(root, [])
        return ans
        
        