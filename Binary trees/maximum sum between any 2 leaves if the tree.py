
# this code runs for only +ve values of data

def dfs(root):
    global ans
    global cnt
    
    if root == None:
        return 0
    
    if root.left == None and root.right == None:
        cnt += 1
    
    lsum = root.val + dfs(root.left)
    rsum = root.val + dfs(root.right)
    
    ans = max(ans, lsum + rsum - root.val)
    
    if lsum > rsum:
        return lsum
    else:
        return rsum
    
    
def findMaxSumPath(root):    
    # Write your code here.
    global ans, cnt
    cnt = 0
    sum = 0
    ans = -1e9
    dfs(root)
    if cnt > 1:
        return ans
    else:
        return -1