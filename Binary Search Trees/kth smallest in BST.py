
def solve(root, k):
    global cnt, ans
    if root == None:
        return
    solve(root.left, k)
    cnt += 1
    if cnt > k:
        return
    if cnt == k:
        ans = root.data
        cnt += 1
        return
    solve(root.right, k)

def kthSmallest(root, k):
    #  Write the code here.
    global cnt, ans
    cnt = 0
    ans = -1
    solve(root, k)
    
    return ans