
def subset(i, arr, n, k, li, temp, sum):
    if i == n:
        if sum == k:
            li.append(temp[:])
        return
    temp.append(arr[i])
    subset(i+1, arr, n, k, li, temp, sum + arr[i])
    temp.pop()
    
#     while i+1 < n and arr[i] == arr[i+1]:
#         i += 1
        
    subset(i+1, arr, n, k, li, temp, sum)
    

def findSubsetsThatSumToK(arr, n, k) :
    # Write your code here.
#     arr.sort()
    temp = []
    li = []
    subset(0, arr, n, k, li, temp, 0)
    
    return li