
def solve(root, d):
    if root == None:
        return
    st = []
    st.append((root, (0, 0)))
    
    while len(st) != 0:
        top = st.pop()
        node = top[0]
        ver = top[1][0]
        lev = top[1][1]
        if ver not in d.keys():
            d1 = {}
            d1[lev] = [node.data]
            d[ver] = d1
        else:
            if lev not in d[ver].keys():
                d[ver][lev] = [node.data]
            else:
                d[ver][lev].append(node.data)
        
        if node.right != None:
            st.append((node.right, (ver+1, lev+1)))
        if node.left != None:
            st.append((node.left, (ver-1, lev+1)))
        
    ans = []
    l = sorted(d)
    for i in l:
        l1 = sorted(d[i])
        for j in l1:
            temp = d[i][j]
            for e in temp:
                ans.append(e)
    return ans
    
def verticalOrderTraversal(root):
	# Write your code here
	# Return a list
    d = {}
    ans = solve(root, d)
    return ans
    