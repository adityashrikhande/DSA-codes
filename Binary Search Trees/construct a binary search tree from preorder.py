
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def nextGreater(arr,n):
    #Your code goes here
    st = []
    ans = [0]*n
    for i in range(n-1, -1, -1):
        while len(st) != 0 and st[-1][0] <= arr[i]:
            st.pop()
        
        if len(st) != 0:
            ans[i] = st[-1][1]
        else:
            ans[i] = n
        
        st.append((arr[i], i))
    return ans
        
def Build(arr, nge, start, end):
    if start > end:
        return None
    
    split = nge[start]
    
    root = TreeNode(arr[start])
    
    root.left = Build(arr, nge, start+1, split-1)
    root.right = Build(arr, nge, split, end)
    
    return root

def preOrderTree(preOrder: list[int]) :
    # Write your code here
    n = len(preOrder)
    nge = nextGreater(preOrder, n)
    return Build(preOrder, nge, 0, n-1)