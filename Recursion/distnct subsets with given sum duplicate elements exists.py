
def subset(i, arr, n, target, sett, ans, sum):
    if i == n:
        if sum == target:
            ans.append(sett[:])
        return
    
    sett.append(arr[i])
    subset(i+1, arr, n, target, sett, ans, sum + arr[i])
    sett.pop()
    
    while i+1 < n and arr[i] == arr[i+1]:
        i += 1
    
    subset(i+1, arr, n, target, sett, ans, sum)

def combinationSum2(arr, n, target):
    # write your code here
    ans = []
    sett = []
    arr.sort()
    subset(0, arr, n, target, sett, ans, 0)
    