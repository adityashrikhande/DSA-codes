
def connectNodes(root):
    # Write your code here.
    st1 = [root]
    root.next = None
    st2 = []
    while True:
        while len(st1) > 0:
            node = st1.pop(0)
            if node.left != None:
                st2.append(node.left)
            if node.right != None:
                st2.append(node.right)
        if len(st2) == 0:
            break
        st1 = st2[:]
        while len(st2) > 1:
            first = st2.pop(0)
            second = st2[0]
            first.next = second
        temp = st2.pop()
        temp.next = None
        st2 = []
        
    return root