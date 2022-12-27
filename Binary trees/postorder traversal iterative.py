
def postorder(root):
    post = []
    st1 = []
    st2 = []
    st1.append(root)
    
    while len(st1) != 0:
        curr = st1.pop()
        st2.append(curr)
        if curr.left != None:
            st1.append(curr.left)
        if curr.right != None:
            st1.append(curr.right)
    
    while len(st2) != 0:
        post.append(st2.pop().val)
        
    return post


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ans = postorder(root)
        return ans
        