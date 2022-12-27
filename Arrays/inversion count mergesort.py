
def merge(arr, temp, left, mid, right):
    
    i = left
    j = mid
    k = left
    inv = 0
    
    while i <= mid-1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            inv += mid-i
    
    while i <= mid-1:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
        
    for i in range(left, right+1):
        arr[i] = temp[i]
        
    return inv

def mergesort(arr, temp, left, right):
    
    mid = (left + right)//2
    inv_cnt = 0
    if left < right:
        inv_cnt += mergesort(arr, temp, left, mid)
        inv_cnt += mergesort(arr, temp, mid+1, right)
        
        inv_cnt += merge(arr, temp, left, mid+1, right)
    
    return inv_cnt
    

def getInversions(arr, n):
	# Write your code here.
    temp = [0]*n
    return mergesort(arr, temp, 0, n-1)
