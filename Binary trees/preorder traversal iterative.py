
def preorder(root, st):
    pre = []
    st.append(root)
    while len(st) != 0:
        curr = st.pop()
        pre.append(curr.val)
        if curr.right != None:
            st.append(curr.right)
        if curr.left != None:
            st.append(curr.left)
        
    return pre

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ans = preorder(root, [])
        return ans