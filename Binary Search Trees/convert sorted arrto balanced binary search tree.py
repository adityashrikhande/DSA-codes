
def Build(arr, start, end):
    if start > end:
        return None
    
    anchor = start + (end-start)//2
    root = TreeNode(arr[anchor])
    
    root.left = Build(arr, start, anchor-1)
    root.right = Build(arr, anchor + 1, end)
    
    return root

def sortedArrToBST(arr, n):   
    # Write your code here
    return Build(arr, 0, n-1)
    