
def length(root):
    global cnt
    if root == None:
        return
    length(root.left)
    cnt += 1
    length(root.right)

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
    

def KthLargestNumber(root, k):

	# Write your code here.
    global cnt, ans
    cnt = 0
    ans = -1
    length(root)
    x = cnt-k+1
    cnt = 0
    solve(root, x)
    
    return ans
    