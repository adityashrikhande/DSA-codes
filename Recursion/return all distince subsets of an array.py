
def subset(idx, n, arr, li, temp):
    li.append(temp[:])
    for i in range(idx, n):
        if idx != i and arr[i] == arr[i-1]:
            continue
        temp.append(arr[i])
        subset(i+1, n, arr, li, temp)
        temp.pop()
  
def uniqueSubsets(n :int,arr :list[int]) -> list[list[int]]:
    
    # Write your code here.
    li = []
    temp = []
    arr.sort()
    subset(0, n, arr, li, temp)
    return li
    

# another solution ############################################

def subset(idx, n, arr, li, ds):
    if idx == n:
        li.append(ds[:])
        return
    
    ds.append(arr[idx])
    subset(idx+1, n, arr, li, ds)
    ds.pop()
    
    while idx+1 < n and arr[idx] == arr[idx+1]:
        idx += 1
    
    subset(idx+1, n, arr, li, ds)
        

class Solution(object):
    def subsetsWithDup(self, arr):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li = []
        ds = []
        n = len(arr)
        arr.sort()
        subset(0, n, arr, li, ds)
        return li
        