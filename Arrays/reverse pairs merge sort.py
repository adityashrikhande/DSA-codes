
def merge(arr, temp, left, mid, right):
    
    cnt = 0
    i = left
    j = mid
    k = left
    
    while i < mid and j <= right:
        if arr[i] <= 2*arr[j]:
            i += 1
            k += 1
        else:
            cnt += mid - i
            j += 1
            k += 1
            
    i = left
    j = mid
    k = left
    
    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
                
    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for m in range(left, right+1):
        arr[m] = temp[m]
        
    return cnt
        
        
def mergesort(arr, temp, left, right):
    cnt = 0
    mid = (left+right)//2
    
    if left < right:
        cnt += mergesort(arr, temp, left, mid)
        cnt += mergesort(arr, temp, mid+1, right)
        
        cnt += merge(arr, temp, left, mid+1, right)
    
    return cnt

def reversePairs(arr, n):
    # Write your code here.
    
    temp = [0]*n
    return mergesort(arr, temp, 0, n-1)

